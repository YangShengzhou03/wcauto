import time
from typing import Any, Dict, Optional, List, Union
from enum import Enum


class ResponseStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    ERROR = "error"


class WxResponse:
    
    def __init__(self, success: bool, message: str, data: Optional[Dict[str, Any]] = None, 
                 status: ResponseStatus = ResponseStatus.SUCCESS) -> None:
        self.success = success
        self.message = message
        self.data = data or {}
        self.status = status
        self.timestamp = self.get_timestamp()

    @classmethod
    def success(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(True, message, data, ResponseStatus.SUCCESS)

    @classmethod
    def failure(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(False, message, data, ResponseStatus.FAILURE)

    @classmethod
    def error(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(False, message, data, ResponseStatus.ERROR)

    @classmethod
    def from_exception(cls, exception: Exception, operation: str = "unknown", 
                       target: str = "unknown") -> 'WxResponse':
        return cls.error(
            message=f"{operation}操作失败: {str(exception)}",
            data={
                "operation": operation,
                "target": target,
                "error_type": type(exception).__name__,
                "error_message": str(exception),
                "timestamp": time.time()
            }
        )

    def get_timestamp(self) -> str:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "status": self.status.value,
            "timestamp": self.timestamp
        }

    def to_json(self) -> str:
        import json
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def get_data_value(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def has_data_key(self, key: str) -> bool:
        return key in self.data

    def merge_data(self, additional_data: Dict[str, Any]) -> 'WxResponse':
        self.data.update(additional_data)
        return self

    def with_operation_info(self, operation: str, target: str = "unknown") -> 'WxResponse':
        self.data.update({
            "operation": operation,
            "target": target,
            "timestamp": time.time()
        })
        return self

    def is_success(self) -> bool:
        return self.success

    def is_failure(self) -> bool:
        return not self.success and self.status == ResponseStatus.FAILURE

    def is_error(self) -> bool:
        return not self.success and self.status == ResponseStatus.ERROR

    def get_error_info(self) -> Dict[str, Any]:
        if self.is_error():
            return {
                "error_type": self.data.get("error_type", "unknown"),
                "error_message": self.data.get("error_message", "unknown"),
                "operation": self.data.get("operation", "unknown"),
                "target": self.data.get("target", "unknown")
            }
        return {}

    def get_operation_summary(self) -> str:
        operation = self.data.get("operation", "unknown")
        target = self.data.get("target", "unknown")
        return f"{operation} -> {target}"

    def __str__(self) -> str:
        status_text = {
            ResponseStatus.SUCCESS: "成功",
            ResponseStatus.FAILURE: "失败", 
            ResponseStatus.ERROR: "错误"
        }.get(self.status, "未知")
        
        summary = self.get_operation_summary()
        return f"WxResponse({status_text}): {self.message} [{summary}]"

    def __repr__(self) -> str:
        return (f"WxResponse(success={self.success}, message='{self.message}', "
                f"data={self.data}, status={self.status}, timestamp='{self.timestamp}')")

    def __bool__(self) -> bool:
        return self.success

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, WxResponse):
            return False
        return (self.success == other.success and 
                self.message == other.message and 
                self.data == other.data and 
                self.status == other.status)


class WxResponseCollection:
    
    def __init__(self) -> None:
        self.responses: List[WxResponse] = []

    def add_response(self, response: WxResponse) -> None:
        self.responses.append(response)

    def add_responses(self, responses: List[WxResponse]) -> None:
        self.responses.extend(responses)

    def get_success_count(self) -> int:
        return sum(1 for response in self.responses if response.success)

    def get_failure_count(self) -> int:
        return sum(1 for response in self.responses if response.is_failure())

    def get_error_count(self) -> int:
        return sum(1 for response in self.responses if response.is_error())

    def get_total_count(self) -> int:
        return len(self.responses)

    def get_success_rate(self) -> float:
        if not self.responses:
            return 0.0
        return self.get_success_count() / len(self.responses)

    def get_successful_responses(self) -> List[WxResponse]:
        return [response for response in self.responses if response.success]

    def get_failed_responses(self) -> List[WxResponse]:
        return [response for response in self.responses if response.is_failure()]

    def get_error_responses(self) -> List[WxResponse]:
        return [response for response in self.responses if response.is_error()]

    def get_summary(self) -> Dict[str, Any]:
        return {
            "total_count": self.get_total_count(),
            "success_count": self.get_success_count(),
            "failure_count": self.get_failure_count(),
            "error_count": self.get_error_count(),
            "success_rate": round(self.get_success_rate() * 100, 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }

    def clear(self) -> None:
        self.responses.clear()

    def __len__(self) -> int:
        return len(self.responses)

    def __iter__(self):
        return iter(self.responses)

    def __getitem__(self, index: int) -> WxResponse:
        return self.responses[index]

    def __str__(self) -> str:
        summary = self.get_summary()
        return (f"WxResponseCollection(总计: {summary['total_count']}, "
                f"成功: {summary['success_count']}, "
                f"失败: {summary['failure_count']}, "
                f"错误: {summary['error_count']}, "
                f"成功率: {summary['success_rate']}%)")

    def __repr__(self) -> str:
        return f"WxResponseCollection(responses={len(self.responses)})"