<div align="center">
  <h1>🤖 wcauto - 微信自动化工具</h1>
  
  <p>
    <em>基于 Python 的微信桌面版自动化操作库，支持消息发送、窗口控制等功能</em>
  </p>

  <div>
    <a href="https://github.com/YangShengzhou03/wcauto/stargazers">
      <img src="https://img.shields.io/github/stars/YangShengzhou03/wcauto?style=for-the-badge&logo=github&color=ffd33d&labelColor=000000" alt="GitHub Stars">
    </a>
    <a href="https://github.com/YangShengzhou03/wcauto/forks">
      <img src="https://img.shields.io/github/forks/YangShengzhou03/wcauto?style=for-the-badge&logo=github&color=green&labelColor=000000" alt="GitHub Forks">
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=open-source-initiative&color=blue&labelColor=000000" alt="MIT License">
    </a>
    <a href="https://github.com/YangShengzhou03/wcauto/issues">
      <img src="https://img.shields.io/github/issues/YangShengzhou03/wcauto?style=for-the-badge&logo=github&color=purple&labelColor=000000" alt="GitHub Issues">
    </a>
    <a href="https://github.com/YangShengzhou03/wcauto/pulls">
      <img src="https://img.shields.io/github/issues-pr/YangShengzhou03/wcauto?style=for-the-badge&logo=github&color=orange&labelColor=000000" alt="GitHub Pull Requests">
    </a>
  </div>

  <div>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" alt="Python Version">
    </a>
    <a href="https://pyautogui.readthedocs.io/">
      <img src="https://img.shields.io/badge/PyAutoGUI-0.9.53+-green?style=for-the-badge&logo=python" alt="PyAutoGUI Version">
    </a>
    <a href="https://github.com/yinkaisheng/Python-UIAutomation-for-Windows">
      <img src="https://img.shields.io/badge/UIAutomation-2.0.15+-orange?style=for-the-badge&logo=windows" alt="UIAutomation Version">
    </a>
    <a href="https://pypi.org/project/pyperclip/">
      <img src="https://img.shields.io/badge/Pyperclip-1.8.2+-yellow?style=for-the-badge&logo=python" alt="Pyperclip Version">
    </a>
  </div>

  <br />
  
  [![Star History Chart](https://api.star-history.com/svg?repos=YangShengzhou03/wcauto&type=Date)](https://star-history.com/#YangShengzhou03/wcauto&Date)

</div>

## 目录
1. [✨ 项目概述](#-项目概述)
2. [🚀 功能特性](#-功能特性)
3. [📦 安装使用](#-安装使用)
4. [💡 快速开始](#-快速开始)
5. [🔧 API 文档](#-api-文档)
6. [📁 项目结构](#-项目结构)
7. [⚠️ 注意事项](#️-注意事项)
8. [🤝 参与贡献](#-参与贡献)
9. [📜 开源许可](#-开源许可)

## ✨ 项目概述

**wcauto** 是一个基于 Python 的微信桌面版自动化操作库，专门为 Windows 平台设计。通过模拟用户操作，实现微信消息的自动发送、窗口控制等功能。

**💡 适用场景**
- 自动化消息通知
- 批量消息发送
- 定时消息提醒
- 微信机器人开发
- 自动化测试

## 🚀 功能特性

### 🔧 核心功能
- **微信窗口检测**：自动查找并激活微信窗口
- **消息发送**：支持向指定联系人发送文本消息
- **智能定位**：自动定位消息输入框和发送按钮
- **异常处理**：包含多种异常处理机制，提高稳定性
- **进程检测**：检查微信是否正在运行

### 🛠️ 技术特点
- **多方案兼容**：提供主方案和备用方案，提高成功率
- **智能坐标计算**：根据窗口大小自动计算点击位置
- **剪贴板操作**：使用剪贴板进行文本传输
- **热键模拟**：支持多种键盘快捷键操作

## 📦 安装使用

### 环境要求
- **操作系统**：Windows 10/11
- **Python**：3.8 及以上版本
- **微信版本**：微信桌面版（需要提前安装并登录）

### 安装依赖
```bash
pip install -r requirements.txt
```

依赖包说明：
- `pyautogui>=0.9.53`：鼠标键盘自动化控制
- `pyperclip>=1.8.2`：剪贴板操作
- `uiautomation>=2.0.15`：Windows UI 自动化
- `psutil>=5.8.0`：进程管理

## 💡 快速开始

### 基本用法
```python
from wcauto import WeChat

# 创建微信自动化实例
wx = WeChat()

# 发送消息给指定联系人
result = wx.SendMsg("文件传输助手", "你好，这是一条测试消息！")

if result:
    print("消息发送成功！")
else:
    print("消息发送失败！")
```

### 使用示例
```python
from wcauto import WeChat

# 初始化
wx = WeChat()

# 检查微信是否运行
if wx.check_wechat_running():
    print("微信正在运行")
else:
    print("微信未运行，请先启动微信")

# 发送消息（支持使用发送按钮）
wx.SendMsg("好友名称", "这是一条测试消息", use_send_button=True)
```

## 🔧 API 文档

### WeChat 类

#### `__init__()`
初始化微信自动化实例。

#### `SendMsg(contact_name, message, use_send_button=False)`
向指定联系人发送消息。

**参数：**
- `contact_name` (str): 联系人名称
- `message` (str): 要发送的消息内容
- `use_send_button` (bool): 是否使用发送按钮（默认使用回车键）

**返回值：**
- `bool`: 发送成功返回 True，失败返回 False

#### `check_wechat_running()`
检查微信进程是否正在运行。

**返回值：**
- `bool`: 微信运行返回 True，否则返回 False

#### `activate_wechat()`
激活微信窗口。

**返回值：**
- `bool`: 激活成功返回 True，失败返回 False

## 📁 项目结构

```
wcauto/
├── wcauto/                 # 核心代码包
│   ├── __init__.py        # 包初始化文件
│   └── wcauto.py          # 主要实现类
├── Application.py         # 使用示例
├── requirements.txt        # 依赖包列表
├── tests/                 # 测试代码
│   ├── __init__.py
│   └── test_wcauto.py
├── LICENSE               # 开源许可证
└── README.md             # 项目说明文档
```

## ⚠️ 注意事项

### 重要提醒
1. **微信版本**：仅支持微信桌面版，不支持网页版微信
2. **窗口要求**：微信窗口需要可见，不能最小化到系统托盘
3. **权限要求**：需要以管理员权限运行程序
4. **兼容性**：不同微信版本可能需要调整坐标计算
5. **使用限制**：请遵守微信使用条款，避免滥用

### 常见问题

**Q: 消息发送失败怎么办？**
A: 
- 检查微信是否已启动并登录
- 确认联系人名称正确
- 尝试使用 `use_send_button=True` 参数
- 检查程序是否以管理员权限运行

**Q: 如何提高发送成功率？**
A:
- 确保微信窗口可见且未被遮挡
- 适当增加操作之间的等待时间
- 使用最新版本的微信

**Q: 支持群聊消息发送吗？**
A: 是的，只需将群聊名称作为 `contact_name` 参数传入即可。

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

### 贡献流程
1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📜 开源许可

本项目采用 [MIT License](LICENSE) 开源协议。

```
MIT License

Copyright (c) 2024 YangShengzhou03

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">
  <sub>Built with ❤️ using Python and automation technologies</sub>
</div>