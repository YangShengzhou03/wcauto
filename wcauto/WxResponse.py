from typing import Any, Dict, Optional
import time


class WxResponse(dict):
    def __init__(self, status: str, message: str, data: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status=status, message=message, data=data or {})

    def __str__(self) -> str:
        return str(self.to_dict())

    def __repr__(self) -> str:
        return str(self.to_dict())

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self['status'],
            'message': self['message'],
            'data': self['data'],
            'timestamp': self.get('timestamp', time.time())
        }

    def __bool__(self) -> bool:
        return self.is_success

    @property
    def is_success(self) -> bool:
        return self['status'] == '成功'

    @property
    def is_failure(self) -> bool:
        return self['status'] == '失败'

    @property
    def is_error(self) -> bool:
        return self['status'] == '错误'

    @classmethod
    def success(cls, message: Optional[str] = None, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(
            status="成功",
            message=message or "操作成功",
            data=data
        )

    @classmethod
    def failure(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(
            status="失败",
            message=message,
            data=data
        )

    @classmethod
    def error(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        return cls(
            status="错误",
            message=message,
            data=data
        )

    def get_operation(self) -> str:
        return self['data'].get('operation', 'unknown')

    def get_target(self) -> str:
        return self['data'].get('target', 'unknown')

    def get_error_type(self) -> str:
        return self['data'].get('error_type', 'unknown')

    def get_timestamp(self) -> float:
        return self['data'].get('timestamp', time.time())