"""
微信自动化响应模块

提供标准化的响应类，用于微信自动化操作的统一返回格式。
"""

"""
微信自动化操作响应类

提供标准化的操作结果格式，包含成功、失败和错误三种状态。
"""

import time
from typing import Any, Dict, Optional


class WxResponse:
    """微信自动化操作响应类。"""

    def __init__(self, success: bool, message: str, data: Optional[Dict[str, Any]] = None) -> None:
        """初始化响应对象。
        
        Args:
            success: 操作是否成功
            message: 响应消息
            data: 响应数据
        """
        self.success = success
        self.message = message
        self.data = data or {}
        self.timestamp = self.get_timestamp()

    @classmethod
    def success(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        """创建成功响应。
        
        Args:
            message: 成功消息
            data: 响应数据
            
        Returns:
            WxResponse: 成功响应对象
        """
        return cls(True, message, data)

    @classmethod
    def failure(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        """创建失败响应。
        
        Args:
            message: 失败消息
            data: 响应数据
            
        Returns:
            WxResponse: 失败响应对象
        """
        return cls(False, message, data)

    @classmethod
    def error(cls, message: str, data: Optional[Dict[str, Any]] = None) -> 'WxResponse':
        """创建错误响应。
        
        Args:
            message: 错误消息
            data: 响应数据
            
        Returns:
            WxResponse: 错误响应对象
        """
        return cls(False, message, data)

    def get_timestamp(self) -> str:
        """获取当前时间戳。
        
        Returns:
            str: 格式化时间戳
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式。
        
        Returns:
            Dict[str, Any]: 字典格式的响应数据
        """
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "timestamp": self.timestamp
        }

    def __str__(self) -> str:
        """字符串表示。
        
        Returns:
            str: 响应对象的字符串表示
        """
        status = "成功" if self.success else "失败"
        return f"WxResponse({status}): {self.message}"

    def __repr__(self) -> str:
        """详细字符串表示。
        
        Returns:
            str: 响应对象的详细字符串表示
        """
        return f"WxResponse(success={self.success}, message='{self.message}', data={self.data}, timestamp='{self.timestamp}')"