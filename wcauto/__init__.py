"""
WeChat自动化库 (wcauto)

一个用于自动化微信消息发送的Python库，支持消息和文件发送功能。

示例用法:
    # 使用简化接口
    from wcauto import SendMsg, SendFiles
    
    # 发送消息
    SendMsg("文件传输助手", "你好，这是一条测试消息")
    
    # 发送文件
    SendFiles("example.txt", "文件传输助手")
    
    # 使用类接口（更多自定义选项）
    from wcauto import WeChatBot
    bot = WeChatBot(safe_mode=True)
    bot.send_message("文件传输助手", "自定义配置的消息")
"""

from .wcauto import WeChat

__version__ = "1.0.0"
__author__ = "Your Name"
__all__ = ["WeChat"]