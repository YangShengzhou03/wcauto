<div align="center">
  <h1>wcauto - 微信自动化工具</h1>
  
  <p>
    <em>基于 Python 的微信桌面版自动化操作库，支持消息发送、文件传输、窗口控制等功能</em>
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
    <a href="https://github.com/YangShengzhou03/wcauto/wiki">
      <img src="https://img.shields.io/badge/Wiki-Documentation-blue?style=for-the-badge&logo=github" alt="Wiki Documentation">
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

## 📖 目录

- [✨ 项目概述](#-项目概述)
- [🚀 核心特性](#-核心特性)
- [📦 快速开始](#-快速开始)
- [🔧 安装指南](#-安装指南)
- [💡 使用教程](#-使用教程)
- [📚 API 文档](#-api-文档)
- [🏗️ 架构设计](#️-架构设计)
- [🔍 常见问题](#-常见问题)
- [🤝 参与贡献](#-参与贡献)
- [📜 开源许可](#-开源许可)

## ✨ 项目概述

**wcauto** 是一个基于 Python 的微信桌面版自动化操作库，专门为 Windows 平台设计。通过模拟用户操作，实现微信消息的自动发送、文件传输、窗口控制等功能。

### 💡 适用场景

| 场景类别 | 具体应用 | 优势特点 |
|---------|---------|---------|
| **自动化通知** | 系统监控、定时提醒 | 实时响应、精准推送 |
| **批量操作** | 营销推广、群发通知 | 高效批量、智能调度 |
| **文件传输** | 备份文件、文档同步 | 稳定可靠、支持大文件 |
| **定时任务** | 日程安排、任务提醒 | 精准定时、自动执行 |
| **机器人开发** | 智能客服、自动回复 | 灵活扩展、智能交互 |
| **自动化测试** | 微信功能测试 | 全面覆盖、持续集成 |

### 🎯 设计理念

- **简单易用**：提供直观的 API 接口，降低使用门槛
- **稳定可靠**：多重异常处理机制，确保操作成功率
- **灵活扩展**：模块化设计，支持自定义功能扩展
- **性能优化**：智能缓存和资源管理，提升执行效率
- **安全合规**：遵循微信使用规范，确保合规操作

## 🚀 核心特性

### 🔧 核心功能

#### 微信窗口管理
- **智能窗口检测**：自动查找并激活微信窗口
- **窗口状态监控**：实时监控窗口状态变化
- **多窗口支持**：支持多个微信窗口的切换管理

#### 消息操作
- **文本消息发送**：支持向指定联系人发送文本消息
- **消息内容验证**：自动验证消息发送状态
- **发送方式选择**：支持回车发送和发送按钮两种方式

#### 文件传输
- **文件发送功能**：支持向指定联系人发送文件
- **文件类型支持**：支持常见文档、图片、压缩包等格式
- **传输状态监控**：实时监控文件传输进度

#### 系统集成
- **进程检测**：检查微信是否正在运行
- **异常处理**：包含多种异常处理机制，提高稳定性
- **资源管理**：智能资源释放和内存管理

### 🛠️ 技术特点

#### 自动化技术
- **多方案兼容**：提供主方案和备用方案，提高成功率
- **智能坐标计算**：根据窗口大小自动计算点击位置
- **剪贴板操作**：使用剪贴板进行文本传输
- **热键模拟**：支持多种键盘快捷键操作

#### 稳定性保障
- **重试机制**：自动重试失败操作，提高成功率
- **超时控制**：合理设置操作超时时间
- **错误恢复**：智能错误检测和自动恢复

#### 性能优化
- **异步操作**：支持异步执行提高效率
- **资源复用**：智能缓存和连接复用
- **内存优化**：优化内存使用，减少资源占用

## 📦 快速开始

### 5分钟快速上手

#### 1. 环境准备
确保您的系统满足以下要求：
- Windows 10/11 操作系统
- Python 3.8 或更高版本
- 微信桌面版（已登录）

#### 2. 安装 wcauto

```bash
# 使用 pip 安装最新版本
pip install git+https://github.com/YangShengzhou03/wcauto.git
```

#### 3. 基础使用示例

```python
from wcauto import WeChat

# 创建微信自动化实例
wx = WeChat()

# 发送消息给文件传输助手
result = wx.send_msg("你好，这是一条测试消息！", "文件传输助手")

if result:
    print("✅ 消息发送成功！")
else:
    print("❌ 消息发送失败！")
```

#### 4. 发送文件示例

```python
from wcauto import WeChat

# 初始化微信自动化实例
wx = WeChat()

# 发送文件
result = wx.send_files(r"C:\path\to\file.pdf", "文件传输助手")

if result:
    print("✅ 文件发送成功！")
else:
    print("❌ 文件发送失败！")
```

### 完整功能演示

```python
from wcauto import WeChat
import time

def comprehensive_demo():
    """完整功能演示"""
    wx = WeChat()
    
    # 检查微信运行状态
    if not wx.check_wechat_running():
        print("⚠️ 微信未运行，请先启动微信")
        return
    
    print("✅ 微信正在运行")
    
    # 激活微信窗口
    if wx.activate_wechat():
        print("✅ 微信窗口激活成功")
    else:
        print("❌ 微信窗口激活失败")
        return
    
    # 发送文本消息
    result1 = wx.send_msg("第一条测试消息", "文件传输助手")
    print(f"📨 消息发送结果: {'成功' if result1 else '失败'}")
    
    time.sleep(1)  # 等待1秒
    
    # 使用发送按钮发送消息
    result2 = wx.send_msg("使用发送按钮的消息", "文件传输助手", use_send_button=True)
    print(f"📨 发送按钮消息结果: {'成功' if result2 else '失败'}")
    
    # 发送文件
    # result3 = wx.send_files(r"C:\path\to\test.pdf", "文件传输助手")
    # print(f"📎 文件发送结果: {'成功' if result3 else '失败'}")

if __name__ == "__main__":
    comprehensive_demo()
```

## 🔧 安装指南

### 系统要求

| 组件 | 最低要求 | 推荐配置 | 说明 |
|------|---------|---------|------|
| **操作系统** | Windows 10 | Windows 11 | 仅支持 Windows 平台 |
| **Python** | 3.8 | 3.9+ | 需要安装 Python 环境 |
| **微信版本** | 微信桌面版 | 最新版本 | 需要提前安装并登录 |
| **内存** | 4GB | 8GB+ | 确保系统运行流畅 |
| **屏幕分辨率** | 1366×768 | 1920×1080+ | 确保界面元素正常显示 |

### 安装方法

#### 方法一：pip 安装（推荐）

```bash
# 从 GitHub 安装最新版本
pip install git+https://github.com/YangShengzhou03/wcauto.git

# 或者安装指定版本
pip install wcauto==1.0.0
```

#### 方法二：源码安装（开发模式）

```bash
# 克隆项目
git clone https://github.com/YangShengzhou03/wcauto.git
cd wcauto

# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Windows CMD:
venv\Scripts\activate.bat
# Windows PowerShell:
venv\Scripts\Activate.ps1

# 安装依赖
pip install -r requirements.txt

# 开发模式安装
pip install -e .
```

#### 方法三：Docker 安装（高级）

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "-c", "from wcauto import WeChat; wx = WeChat(); print('wcauto 安装成功！')]"]
```

### 依赖说明

wcauto 依赖于以下 Python 包：

| 依赖包 | 版本要求 | 主要功能 | 官方文档 |
|--------|---------|---------|---------|
| `pyautogui` | >=0.9.53,<1.0.0 | 鼠标键盘自动化控制 | [文档](https://pyautogui.readthedocs.io/) |
| `pyperclip` | >=1.8.2,<2.0.0 | 剪贴板操作 | [文档](https://pypi.org/project/pyperclip/) |
| `uiautomation` | >=2.0.15,<3.0.0 | Windows UI 自动化 | [文档](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows) |
| `psutil` | >=5.8.0,<6.0.0 | 进程管理 | [文档](https://psutil.readthedocs.io/) |
| `pywin32` | >=300,<310 | Windows API 接口 | [文档](https://pypi.org/project/pywin32/) |

### 安装验证

创建验证脚本 `verify_installation.py`：

```python
#!/usr/bin/env python3
"""
wcauto 安装验证脚本
用于验证 wcauto 是否正确安装和配置
"""

import sys
import importlib.util

def check_python_version():
    """检查 Python 版本"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python 版本检查通过: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python 版本过低: {version.major}.{version.minor}.{version.micro}，需要 3.8+")
        return False

def check_dependencies():
    """检查依赖包是否安装"""
    dependencies = [
        ('pyautogui', '0.9.53'),
        ('pyperclip', '1.8.2'),
        ('uiautomation', '2.0.15'),
        ('psutil', '5.8.0'),
        ('pywin32', '300')
    ]
    
    all_installed = True
    for package, min_version in dependencies:
        try:
            spec = importlib.util.find_spec(package)
            if spec is not None:
                print(f"✅ {package} 已安装")
            else:
                print(f"❌ {package} 未安装")
                all_installed = False
        except ImportError:
            print(f"❌ {package} 导入失败")
            all_installed = False
    
    return all_installed

def check_wcauto_import():
    """检查 wcauto 是否能正常导入"""
    try:
        from wcauto import WeChat
        print("✅ wcauto 导入成功")
        return True
    except ImportError as e:
        print(f"❌ wcauto 导入失败: {e}")
        return False

def main():
    """主验证函数"""
    print("🚀 开始验证 wcauto 安装...")
    print("=" * 50)
    
    # 检查 Python 版本
    python_ok = check_python_version()
    
    # 检查依赖包
    deps_ok = check_dependencies()
    
    # 检查 wcauto 导入
    import_ok = check_wcauto_import()
    
    print("=" * 50)
    
    if python_ok and deps_ok and import_ok:
        print("🎉 所有检查通过！wcauto 安装成功！")
        print("💡 接下来可以开始使用 wcauto 进行微信自动化操作")
        return True
    else:
        print("❌ 安装验证失败，请检查上述错误信息")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
```

运行验证脚本：

```bash
python verify_installation.py
```

## 💡 使用教程

### 基础操作

#### 1. 初始化与基本检查

```python
from wcauto import WeChat

# 创建微信自动化实例
wx = WeChat()

# 检查微信是否运行
if not wx.check_wechat_running():
    print("微信未运行，请先启动微信")
    exit(1)

# 激活微信窗口
if not wx.activate_wechat():
    print("无法激活微信窗口")
    exit(1)
```

#### 2. 发送文本消息

```python
# 发送给当前聊天窗口
wx.send_msg("这是一条测试消息")

# 发送给指定联系人
wx.send_msg("你好，这是一条测试消息！", "文件传输助手")

# 使用发送按钮而非回车键
wx.send_msg("使用发送按钮发送的消息", "好友名称", use_send_button=True)
```

#### 3. 发送文件

```python
# 发送单个文件
file_path = r"C:\path\to\file.pdf"
result = wx.send_files(file_path, "文件传输助手")

if result:
    print("文件发送成功！")
else:
    print("文件发送失败！")

# 发送给当前聊天
wx.send_files(r"C:\path\to\image.jpg")
```

### 高级应用

#### 1. 批量消息发送

```python
import time

def send_batch_messages(recipient, messages, delay=1):
    """
    批量发送消息给指定联系人
    
    Args:
        recipient (str): 接收者名称
        messages (list): 消息列表
        delay (int): 发送间隔（秒）
    """
    wx = WeChat()
    
    if not wx.check_wechat_running():
        print("微信未运行，请先启动微信")
        return False
    
    success_count = 0
    total_count = len(messages)
    
    for i, msg in enumerate(messages, 1):
        print(f"正在发送第 {i}/{total_count} 条消息...")
        
        if wx.send_msg(msg, recipient):
            success_count += 1
            print(f"✅ 消息发送成功: {msg[:20]}...")
        else:
            print(f"❌ 消息发送失败: {msg[:20]}...")
        
        # 避免发送过快
        if i < total_count:
            time.sleep(delay)
    
    success_rate = (success_count / total_count) * 100
    print(f"📊 批量发送完成: {success_count}/{total_count} 成功 ({success_rate:.1f}%)")
    return success_count == total_count

# 使用示例
messages = [
    "这是第一条消息",
    "这是第二条消息", 
    "这是第三条消息",
    "这是第四条消息",
    "这是第五条消息"
]

send_batch_messages("文件传输助手", messages, delay=2)
```

#### 2. 定时消息发送

```python
import schedule
import time
from datetime import datetime

def send_scheduled_message(recipient, message, schedule_time):
    """
    定时发送消息
    
    Args:
        recipient (str): 接收者名称
        message (str): 消息内容
        schedule_time (str): 定时时间，格式 "HH:MM"
    """
    def job():
        wx = WeChat()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if wx.send_msg(message, recipient):
            print(f"{timestamp} - ✅ 定时消息发送成功")
        else:
            print(f"{timestamp} - ❌ 定时消息发送失败")
    
    schedule.every().day.at(schedule_time).do(job)
    print(f"⏰ 已设置定时消息: {schedule_time} 发送给 {recipient}")
    
    # 保持调度器运行
    while True:
        schedule.run_pending()
        time.sleep(1)

# 使用示例（取消注释以启用）
# send_scheduled_message("文件传输助手", "这是一条定时消息", "14:30")
```

#### 3. 文件批量发送

```python
import os
import time

def send_batch_files(recipient, file_paths, delay=2):
    """
    批量发送文件给指定联系人
    
    Args:
        recipient (str): 接收者名称
        file_paths (list): 文件路径列表
        delay (int): 发送间隔（秒）
    """
    wx = WeChat()
    
    if not wx.check_wechat_running():
        print("微信未运行，请先启动微信")
        return False
    
    success_count = 0
    total_count = len(file_paths)
    
    for i, file_path in enumerate(file_paths, 1):
        filename = os.path.basename(file_path)
        print(f"正在发送第 {i}/{total_count} 个文件: {filename}")
        
        if not os.path.exists(file_path):
            print(f"❌ 文件不存在: {file_path}")
            continue
        
        if wx.send_files(file_path, recipient):
            success_count += 1
            print(f"✅ 文件发送成功: {filename}")
        else:
            print(f"❌ 文件发送失败: {filename}")
        
        # 避免发送过快
        if i < total_count:
            time.sleep(delay)
    
    success_rate = (success_count / total_count) * 100
    print(f"📊 批量发送完成: {success_count}/{total_count} 成功 ({success_rate:.1f}%)")
    return success_count > 0

# 使用示例
files = [
    r"C:\path\to\file1.pdf",
    r"C:\path\to\file2.jpg", 
    r"C:\path\to\file3.docx"
]

send_batch_files("文件传输助手", files, delay=3)
```

#### 4. 消息发送状态监控

```python
def send_with_retry(message, recipient, max_retries=3, retry_delay=2):
    """
    带重试机制的消息发送
    
    Args:
        message (str): 消息内容
        recipient (str): 接收者名称
        max_retries (int): 最大重试次数
        retry_delay (int): 重试间隔（秒）
    """
    wx = WeChat()
    
    for attempt in range(max_retries):
        try:
            print(f"🔄 尝试发送消息 (第 {attempt + 1}/{max_retries} 次)...")
            
            if wx.send_msg(message, recipient):
                print(f"✅ 消息发送成功 (尝试 {attempt + 1}/{max_retries})")
                return True
            else:
                print(f"❌ 消息发送失败 (尝试 {attempt + 1}/{max_retries})")
                
        except Exception as e:
            print(f"⚠️ 发送异常 (尝试 {attempt + 1}/{max_retries}): {e}")
        
        # 如果不是最后一次尝试，等待后重试
        if attempt < max_retries - 1:
            print(f"⏳ 等待 {retry_delay} 秒后重试...")
            time.sleep(retry_delay)
    
    print(f"💥 消息发送失败，已达到最大重试次数 {max_retries}")
    return False

# 使用示例
send_with_retry("这是一条重要的测试消息", "文件传输助手", max_retries=3)
```

#### 5. 自定义日志配置

```python
import logging

def setup_custom_logger(log_file='wcauto.log', level=logging.INFO):
    """
    设置自定义日志配置
    
    Args:
        log_file (str): 日志文件路径
        level: 日志级别
    """
    # 创建日志记录器
    logger = logging.getLogger('wcauto')
    logger.setLevel(level)
    
    # 避免重复添加处理器
    if logger.handlers:
        return logger
    
    # 创建文件处理器
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(level)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # 创建格式化器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加处理器到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# 使用示例
logger = setup_custom_logger()
wx = WeChat()
logger.info("微信自动化实例已创建")
```

### 实际应用场景

#### 1. 工作报告自动发送

```python
import datetime

def send_daily_report(recipient="上级领导"):
    """发送每日工作报告"""
    # 生成报告内容
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report_content = f"""
📊 工作日报 - {today}

✅ 今日完成工作：
1. 完成项目A的需求分析
2. 修复了3个关键bug
3. 参与团队技术分享会议
4. 代码审查和优化

📅 明日计划：
1. 开始项目B的核心功能开发
2. 进行系统性能测试
3. 编写技术文档

💡 问题与建议：
- 建议优化开发环境配置
- 需要更多测试资源支持

感谢审阅！
    """
    
    # 发送报告
    wx = WeChat()
    if wx.send_msg(report_content, recipient):
        print("✅ 日报发送成功")
        return True
    else:
        print("❌ 日报发送失败")
        return False

# 每天下午6点发送日报
# schedule.every().day.at("18:00").do(send_daily_report)
```

#### 2. 系统监控通知

```python
import psutil

def system_monitor(threshold=80):
    """系统资源监控并发送通知"""
    # 获取系统资源使用情况
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # 构建通知消息
    message = f"""
🚨 系统资源监控报告

📊 当前资源使用情况：
• CPU使用率: {cpu_percent}%
• 内存使用率: {memory.percent}%
• 磁盘使用率: {disk.percent}%

⚠️ 注意：资源使用率超过 {threshold}%，请及时处理！
    """
    
    # 当资源使用率超过阈值时发送通知
    if cpu_percent > threshold or memory.percent > threshold or disk.percent > threshold:
        wx = WeChat()
        if wx.send_msg(message, "系统管理员"):
            print("✅ 系统监控通知发送成功")
        else:
            print("❌ 系统监控通知发送失败")
    else:
        print("✅ 系统资源使用正常")

# 每30分钟检查一次系统资源
# while True:
#     system_monitor()
#     time.sleep(1800)  # 30分钟
```

#### 3. 文件自动备份通知

```python
import shutil
import os
from datetime import datetime

def backup_and_notify(source_dir, backup_dir, recipient):
    """
    备份文件并发送通知
    
    Args:
        source_dir (str): 源目录
        backup_dir (str): 备份目录
        recipient (str): 通知接收者
    """
    try:
        # 创建备份目录（如果不存在）
        os.makedirs(backup_dir, exist_ok=True)
        
        # 获取当前时间作为备份文件夹名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
        
        print(f"🔄 开始备份: {source_dir} -> {backup_path}")
        
        # 执行备份
        shutil.copytree(source_dir, backup_path)
        
        # 计算备份文件大小
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(backup_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        
        # 转换为MB
        total_size_mb = total_size / (1024 * 1024)
        
        # 发送通知
        message = f"""
✅ 文件备份完成！

📁 备份信息：
• 源目录: {source_dir}
• 备份目录: {backup_path}
• 备份大小: {total_size_mb:.2f} MB
• 备份时间: {timestamp}

💾 备份成功，请检查文件完整性。
        """
        
        wx = WeChat()
        if wx.send_msg(message, recipient):
            print("✅ 备份通知发送成功")
        else:
            print("❌ 备份通知发送失败")
            
    except Exception as e:
        error_message = f"❌ 文件备份失败: {str(e)}"
        print(error_message)
        
        # 发送错误通知
        wx = WeChat()
        wx.send_msg(error_message, recipient)

# 使用示例
# backup_and_notify(r"C:\重要文档", r"D:\备份\重要文档", "文件传输助手")
```

## 📚 API 文档

### WeChat 类

#### 构造函数

```python
WeChat()
```
创建微信自动化实例。

#### 方法列表

##### `check_wechat_running()`
检查微信进程是否正在运行。

**返回值：**
- `bool`: True 表示微信正在运行，False 表示未运行

**示例：**
```python
wx = WeChat()
if wx.check_wechat_running():
    print("微信正在运行")
else:
    print("微信未运行")
```

##### `activate_wechat()`
激活微信窗口。

**返回值：**
- `bool`: True 表示激活成功，False 表示激活失败

**示例：**
```python
wx = WeChat()
if wx.activate_wechat():
    print("微信窗口激活成功")
```

##### `send_msg(msg, who=None, use_send_button=False)`
发送文本消息。

**参数：**
- `msg` (str): 要发送的消息内容
- `who` (str, optional): 接收者名称，如果为 None 则发送给当前聊天窗口
- `use_send_button` (bool, optional): 是否使用发送按钮，默认为 False（使用回车键）

**返回值：**
- `WxResponse`: 发送结果对象

**示例：**
```python
wx = WeChat()
result = wx.send_msg("Hello World", "文件传输助手")
if result.success:
    print("消息发送成功")
```

##### `send_files(filepath, who=None)`
发送文件。

**参数：**
- `filepath` (str): 要发送的文件路径
- `who` (str, optional): 接收者名称，如果为 None 则发送给当前聊天窗口

**返回值：**
- `WxResponse`: 发送结果对象

**示例：**
```python
wx = WeChat()
result = wx.send_files(r"C:\test.pdf", "文件传输助手")
if result.success:
    print("文件发送成功")
```

### WxResponse 类

微信操作响应对象。

#### 属性

- `success` (bool): 操作是否成功
- `message` (str): 操作结果描述
- `timestamp`