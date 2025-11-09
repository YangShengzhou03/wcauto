import time
from typing import Any, Dict, Optional


class WxResponse:
    def __init__(self, success: bool, message: str, data: Optional[Dict[str, Any]] = None) -> None:
        self.success = success
        self.message = message
        self.data = data or {}
        self.timestamp = self.get_timestamp()

    @classmethod
    def success(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(True, message, data)

    @classmethod
    def failure(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(False, message, data)

    @classmethod
    def error(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(False, message, data)

    def get_timestamp(self) -> str:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "timestamp": self.timestamp
        }

    def __str__(self) -> str:
        status = "成功" if self.success else "失败"
        return f"WxResponse({status}): {self.message}"

    def __repr__(self) -> str:
        return f"WxResponse(success={self.success}, message='{self.message}', data={self.data}, timestamp='{self.timestamp}')"