# wcauto - WeChat Automation Library

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-beta-orange.svg)](https://github.com/yourusername/wcauto)

`wcauto` 是一个用于自动化微信消息发送的Python库，通过RPA技术实现高速、高准确度的消息发送。

## 功能特点

- 🚀 **高速发送**：优化的发送流程，减少不必要的延迟
- 🎯 **高准确度**：多重定位和备用方案，确保操作成功
- 🔧 **灵活配置**：可自定义延迟参数和发送方式
- 🛡️ **错误处理**：完善的异常处理和日志记录
- 📝 **简单易用**：简洁的API设计，易于集成

## 安装

```bash
pip install wcauto
```

或者从源码安装：

```bash
git clone https://github.com/yourusername/wcauto.git
cd wcauto
pip install -e .
```

## 快速开始

### 基本用法

```python
from wcauto import WeChatBot

# 创建机器人实例
bot = WeChatBot()

# 发送消息
bot.send_message("文件传输助手", "你好，这是一条测试消息！")
```

### 高级配置

```python
from wcauto import WeChatBot

# 创建带有自定义配置的机器人实例
bot = WeChatBot(
    search_delay=1.0,      # 搜索联系人时的延迟时间(秒)
    input_delay=0.2,       # 输入文本时的延迟时间(秒)
    send_delay=0.3,        # 发送消息时的延迟时间(秒)
    use_send_button=True,  # 使用发送按钮而不是Enter键
    safe_mode=False        # 关闭安全模式以提高速度
)

# 发送消息
success = bot.send_message("联系人名称", "消息内容")
if success:
    print("消息发送成功！")
else:
    print("消息发送失败！")
```

### 批量发送

```python
from wcauto import WeChatBot

bot = WeChatBot(safe_mode=False)  # 关闭安全模式以提高批量发送速度

contacts = ["联系人1", "联系人2", "联系人3"]
message = "这是一条批量发送的消息"

for contact in contacts:
    success = bot.send_message(contact, message)
    if success:
        print(f"已成功发送给 {contact}")
    else:
        print(f"发送给 {contact} 失败")
```

## API 文档

### WeChatBot 类

#### 构造函数

```python
WeChatBot(
    search_delay=1.5, 
    input_delay=0.3, 
    send_delay=0.5,
    use_send_button=False,
    safe_mode=True
)
```

**参数：**
- `search_delay` (float): 搜索联系人时的延迟时间，默认为1.5秒
- `input_delay` (float): 输入文本时的延迟时间，默认为0.3秒
- `send_delay` (float): 发送消息时的延迟时间，默认为0.5秒
- `use_send_button` (bool): 是否使用发送按钮而不是Enter键，默认为False
- `safe_mode` (bool): 是否启用安全模式，会增加额外的延迟以确保稳定性，默认为True

#### 方法

##### send_message(contact_name, message, use_send_button=None)

发送消息给指定联系人

**参数：**
- `contact_name` (str): 联系人名称
- `message` (str): 消息内容
- `use_send_button` (bool, optional): 是否使用发送按钮，如果为None则使用初始化时的设置

**返回：**
- `bool`: 是否成功发送

##### SendMsg(contact_name, message, use_send_button=False)

兼容性方法，功能与`send_message`相同

**参数：**
- `contact_name` (str): 联系人名称
- `message` (str): 消息内容
- `use_send_button` (bool): 是否使用发送按钮，默认为False

**返回：**
- `bool`: 是否成功发送

##### check_wechat_running()

检查微信是否正在运行

**返回：**
- `bool`: 微信是否正在运行

## 注意事项

1. **系统要求**：本库仅支持Windows系统
2. **微信要求**：需要安装并登录微信桌面版
3. **屏幕分辨率**：库会自动适应不同的屏幕分辨率
4. **使用前准备**：确保微信窗口可见且未被最小化
5. **权限要求**：可能需要管理员权限才能正常操作

## 性能优化建议

1. **调整延迟参数**：根据您的系统性能和网络状况，适当调整`search_delay`、`input_delay`和`send_delay`参数
2. **关闭安全模式**：在稳定的环境下，可以设置`safe_mode=False`以提高发送速度
3. **批量发送**：对于批量发送任务，建议先测试少量联系人，确认无误后再进行大规模发送

## 常见问题

### Q: 消息发送失败怎么办？
A: 首先检查微信是否正常运行，然后尝试增加延迟参数或启用安全模式。如果问题仍然存在，请查看日志以获取更多信息。

### Q: 如何提高发送速度？
A: 可以尝试减少延迟参数或关闭安全模式。但请注意，过快的速度可能导致操作失败。

### Q: 支持群聊吗？
A: 是的，您可以将群聊名称作为联系人名称来发送消息。

## 许可证

本项目采用MIT许可证。详情请参阅[LICENSE](LICENSE)文件。

## 贡献

欢迎提交Issue和Pull Request来帮助改进本项目。

## 更新日志

### v1.0.0 (2023-XX-XX)
- 初始版本发布
- 支持基本的微信消息发送功能
- 添加错误处理和日志记录
- 提供灵活的配置选项