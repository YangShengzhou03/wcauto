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
- [🚀 功能特性](#-功能特性)
- [📦 快速开始](#-快速开始)
- [🔧 安装指南](#-安装指南)
- [💡 使用教程](#-使用教程)
- [📚 API 文档](#-api-文档)
- [🏗️ 架构设计](#️-架构设计)
- [🚀 部署指南](#-部署指南)
- [🔍 常见问题](#-常见问题)
- [🤝 参与贡献](#-参与贡献)
- [📜 开源许可](#-开源许可)
- [👥 贡献者](#-贡献者)

## ✨ 项目概述

**wcauto** 是一个基于 Python 的微信桌面版自动化操作库，专门为 Windows 平台设计。通过模拟用户操作，实现微信消息的自动发送、文件传输、窗口控制等功能。

### 💡 适用场景
- **自动化消息通知**：系统监控、定时提醒
- **批量消息发送**：营销推广、群发通知
- **文件自动传输**：备份文件、文档同步
- **定时消息提醒**：日程安排、任务提醒
- **微信机器人开发**：智能客服、自动回复
- **自动化测试**：微信功能测试、集成测试

### 🎯 设计理念
- **简单易用**：提供直观的 API 接口，降低使用门槛
- **稳定可靠**：多重异常处理机制，确保操作成功率
- **灵活扩展**：模块化设计，支持自定义功能扩展
- **性能优化**：智能缓存和资源管理，提升执行效率

## 🚀 功能特性

### 🔧 核心功能
- **微信窗口检测**：自动查找并激活微信窗口
- **消息发送**：支持向指定联系人发送文本消息
- **文件传输**：支持向指定联系人发送文件
- **智能定位**：自动定位消息输入框和发送按钮
- **异常处理**：包含多种异常处理机制，提高稳定性
- **进程检测**：检查微信是否正在运行

### 🛠️ 技术特点
- **多方案兼容**：提供主方案和备用方案，提高成功率
- **智能坐标计算**：根据窗口大小自动计算点击位置
- **剪贴板操作**：使用剪贴板进行文本传输
- **热键模拟**：支持多种键盘快捷键操作
- **文件处理**：支持通过剪贴板传输文件

## 📦 快速开始

### 基本用法

```python
from wcauto import WeChat

# 创建微信自动化实例
wx = WeChat()

# 发送消息给指定联系人
result = wx.SendMsg("你好，这是一条测试消息！", "文件传输助手")

if result:
    print("消息发送成功！")
else:
    print("消息发送失败！")
```

### 发送文件

```python
from wcauto import WeChat

# 初始化
wx = WeChat()

# 发送文件给指定联系人
result = wx.SendFiles(r"C:\path\to\file.pdf", "文件传输助手")

if result:
    print("文件发送成功！")
else:
    print("文件发送失败！")
```

### 完整示例

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
wx.SendMsg("这是一条测试消息", "好友名称", use_send_button=True)
```

## 🔧 安装指南

### 环境要求

| 组件 | 要求 | 说明 |
|------|------|------|
| **操作系统** | Windows 10/11 | 仅支持 Windows 平台 |
| **Python** | 3.8 及以上版本 | 推荐使用 Python 3.9+ |
| **微信版本** | 微信桌面版 | 需要提前安装并登录 |

### 安装方法

#### 方法一：使用 pip 安装（推荐）

```bash
# 从 GitHub 安装最新版本
pip install git+https://github.com/YangShengzhou03/wcauto.git

# 或者从 PyPI 安装（如果已发布）
# pip install wcauto
```

#### 方法二：源码安装

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

# 安装包
pip install -e .
```

### 依赖说明

| 依赖包 | 版本 | 用途 |
|--------|------|------|
| `pyautogui` | >=0.9.53 | 鼠标键盘自动化控制 |
| `pyperclip` | >=1.8.2 | 剪贴板操作 |
| `uiautomation` | >=2.0.15 | Windows UI 自动化 |
| `psutil` | >=5.8.0 | 进程管理 |
| `pywin32` | >=300 | Windows API 接口 |

### 验证安装

```python
# 创建验证脚本 verify_installation.py
from wcauto import WeChat

def verify_installation():
    """验证安装是否成功"""
    try:
        wx = WeChat()
        print("✅ wcauto 导入成功")
        
        # 检查微信进程
        if wx.check_wechat_running():
            print("✅ 微信进程检测正常")
        else:
            print("⚠️ 微信未运行（正常情况）")
            
        print("✅ 安装验证通过！")
        return True
        
    except Exception as e:
        print(f"❌ 安装验证失败: {e}")
        return False

if __name__ == "__main__":
    verify_installation()
```

## 💡 快速开始

### 基本用法
```python
from wcauto import WeChat

# 创建微信自动化实例
wx = WeChat()

# 发送消息给指定联系人
result = wx.SendMsg("你好，这是一条测试消息！", "文件传输助手")

if result:
    print("消息发送成功！")
else:
    print("消息发送失败！")
```

### 发送文件
```python
from wcauto import WeChat

# 初始化
wx = WeChat()

# 发送文件给指定联系人
result = wx.SendFiles(r"C:\path\to\file.pdf", "文件传输助手")

if result:
    print("文件发送成功！")
else:
    print("文件发送失败！")
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
wx.SendMsg("这是一条测试消息", "好友名称", use_send_button=True)
```

## 🔧 详细使用方法

### 基础用法

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
wx.SendMsg("这是一条测试消息")

# 发送给指定联系人
wx.SendMsg("你好，这是一条测试消息！", "文件传输助手")

# 使用发送按钮而非回车键
wx.SendMsg("使用发送按钮发送的消息", "好友名称", use_send_button=True)
```

#### 3. 发送文件

```python
# 发送单个文件
file_path = r"C:\path\to\file.pdf"
result = wx.SendFiles(file_path, "文件传输助手")

if result:
    print("文件发送成功！")
else:
    print("文件发送失败！")

# 发送给当前聊天
wx.SendFiles(r"C:\path\to\image.jpg")
```

### 高级用法

#### 1. 批量消息发送

```python
def send_batch_messages(recipient, messages):
    """
    批量发送消息给指定联系人
    
    Args:
        recipient (str): 接收者名称
        messages (list): 消息列表
    """
    wx = WeChat()
    
    if not wx.check_wechat_running():
        print("微信未运行，请先启动微信")
        return False
    
    success_count = 0
    for msg in messages:
        if wx.SendMsg(msg, recipient):
            success_count += 1
            print(f"消息发送成功: {msg[:20]}...")
            time.sleep(1)  # 避免发送过快
        else:
            print(f"消息发送失败: {msg[:20]}...")
    
    print(f"批量发送完成: {success_count}/{len(messages)} 成功")
    return success_count == len(messages)

# 使用示例
messages = [
    "这是第一条消息",
    "这是第二条消息",
    "这是第三条消息"
]
send_batch_messages("文件传输助手", messages)
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
        if wx.SendMsg(message, recipient):
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 消息发送成功")
        else:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 消息发送失败")
    
    schedule.every().day.at(schedule_time).do(job)
    print(f"已设置定时消息: {schedule_time} 发送给 {recipient}")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

# 使用示例
# send_scheduled_message("文件传输助手", "这是一条定时消息", "14:30")
```

#### 3. 文件批量发送

```python
def send_batch_files(recipient, file_paths):
    """
    批量发送文件给指定联系人
    
    Args:
        recipient (str): 接收者名称
        file_paths (list): 文件路径列表
    """
    wx = WeChat()
    
    if not wx.check_wechat_running():
        print("微信未运行，请先启动微信")
        return False
    
    success_count = 0
    for file_path in file_paths:
        if os.path.exists(file_path):
            if wx.SendFiles(file_path, recipient):
                success_count += 1
                print(f"文件发送成功: {os.path.basename(file_path)}")
                time.sleep(2)  # 避免发送过快
            else:
                print(f"文件发送失败: {os.path.basename(file_path)}")
        else:
            print(f"文件不存在: {file_path}")
    
    print(f"批量发送完成: {success_count}/{len(file_paths)} 成功")
    return success_count > 0

# 使用示例
files = [
    r"C:\path\to\file1.pdf",
    r"C:\path\to\file2.jpg",
    r"C:\path\to\file3.docx"
]
send_batch_files("文件传输助手", files)
```

#### 4. 消息发送状态监控

```python
def send_with_retry(message, recipient, max_retries=3):
    """
    带重试机制的消息发送
    
    Args:
        message (str): 消息内容
        recipient (str): 接收者名称
        max_retries (int): 最大重试次数
    """
    wx = WeChat()
    
    for attempt in range(max_retries):
        try:
            if wx.SendMsg(message, recipient):
                print(f"消息发送成功 (尝试 {attempt + 1}/{max_retries})")
                return True
            else:
                print(f"消息发送失败 (尝试 {attempt + 1}/{max_retries})")
        except Exception as e:
            print(f"发送异常 (尝试 {attempt + 1}/{max_retries}): {e}")
        
        if attempt < max_retries - 1:
            print("等待 2 秒后重试...")
            time.sleep(2)
    
    print(f"消息发送失败，已达到最大重试次数 {max_retries}")
    return False

# 使用示例
send_with_retry("这是一条重要的测试消息", "文件传输助手")
```

#### 5. 自定义日志配置

```python
import logging

def setup_custom_logger():
    """设置自定义日志配置"""
    # 创建日志记录器
    logger = logging.getLogger('wcauto')
    logger.setLevel(logging.INFO)
    
    # 创建文件处理器
    file_handler = logging.FileHandler('wcauto.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
def send_daily_report():
    """发送每日工作报告"""
    import datetime
    
    # 生成报告内容
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report_content = f"""
    工作日报 - {today}
    
    今日完成工作：
    1. 完成项目A的需求分析
    2. 修复了3个bug
    3. 参与团队会议
    
    明日计划：
    1. 开始项目B的开发
    2. 代码审查
    
    问题与建议：
    暂无
    """
    
    # 发送报告
    wx = WeChat()
    if wx.SendMsg(report_content, "上级领导"):
        print("日报发送成功")
    else:
        print("日报发送失败")

# 每天下午6点发送日报
# schedule.every().day.at("18:00").do(send_daily_report)
```

#### 2. 系统监控通知

```python
import psutil

def system_monitor():
    """系统资源监控并发送通知"""
    # 获取系统资源使用情况
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # 构建通知消息
    message = f"""
    系统资源监控报告：
    
    CPU使用率: {cpu_percent}%
    内存使用率: {memory.percent}%
    磁盘使用率: {disk.percent}%
    
    注意：如果资源使用率过高，请及时处理！
    """
    
    # 当资源使用率超过阈值时发送通知
    if cpu_percent > 80 or memory.percent > 80 or disk.percent > 80:
        wx = WeChat()
        wx.SendMsg(message, "系统管理员")
        print("系统资源使用率过高，已发送通知")
    else:
        print("系统资源使用正常")

# 每30分钟检查一次系统资源
# while True:
#     system_monitor()
#     time.sleep(1800)  # 30分钟
```

#### 3. 文件自动备份通知

```python
import shutil
import os

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
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
        
        # 执行备份
        shutil.copytree(source_dir, backup_path)
        
        # 计算备份文件大小
        total_size = sum(os.path.getsize(os.path.join(dirpath, filename)) 
                         for dirpath, dirnames, filenames in os.walk(backup_path) 
                         for filename in filenames)
        
        # 转换为MB
        total_size_mb = total_size / (1024 * 1024)
        
        # 发送通知
        message = f"""
        文件备份完成！
        
        源目录: {source_dir}
        备份目录: {backup_path}
        备份大小: {total_size_mb:.2f} MB
        备份时间: {timestamp}
        
        备份成功，请检查文件完整性。
        """
        
        wx = WeChat()
        if wx.SendMsg(message, recipient):
            print("备份通知发送成功")
        else:
            print("备份通知发送失败")
            
    except Exception as e:
        error_message = f"文件备份失败: {str(e)}"
        print(error_message)
        
        # 发送错误通知
        wx = WeChat()
        wx.SendMsg(error_message, recipient)

# backup_and_notify(r"C:\重要文档", r"D:\备份\重要文档", "文件传输助手")
```

## 🚀 部署指南

### 开发环境部署

#### 1. 环境准备

**系统要求：**
- Windows 10/11 (64位)
- Python 3.8 或更高版本
- 微信桌面版 (已登录)

**Python 环境配置：**
```bash
# 检查 Python 版本
python --version

# 如果未安装 Python，请从 https://www.python.org/downloads/ 下载安装
```

#### 2. 项目克隆与安装

```bash
# 克隆项目
git clone https://github.com/YangShengzhou03/wcauto.git
cd wcauto

# 创建虚拟环境 (推荐)
python -m venv venv

# 激活虚拟环境
# Windows CMD:
venv\Scripts\activate.bat
# Windows PowerShell:
venv\Scripts\Activate.ps1

# 安装依赖
pip install -r requirements.txt
```

#### 3. 开发环境测试

```python
# 创建测试脚本 test_development.py
from wcauto import WeChat

def test_deployment():
    """测试开发环境部署是否成功"""
    wx = WeChat()
    
    # 检查微信是否运行
    if not wx.check_wechat_running():
        print("❌ 微信未运行，请先启动微信并登录")
        return False
    
    # 激活微信窗口
    if not wx.activate_wechat():
        print("❌ 无法激活微信窗口")
        return False
    
    # 发送测试消息
    result = wx.SendMsg("开发环境测试消息", "文件传输助手")
    
    if result:
        print("✅ 开发环境部署成功！")
        return True
    else:
        print("❌ 消息发送失败，请检查配置")
        return False

if __name__ == "__main__":
    test_deployment()
```

### 生产环境部署

#### 1. 打包为可执行文件

使用 PyInstaller 将项目打包为独立的可执行文件：

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包为单个可执行文件
pyinstaller --onefile --name wcauto_tool wcauto/wcauto.py

# 打包为目录形式（包含依赖）
pyinstaller --name wcauto_tool wcauto/wcauto.py
```

打包后的文件位于 `dist` 目录中，可以直接运行而无需 Python 环境。

#### 2. 创建系统服务

使用 Windows 任务计划程序创建定时任务：

```python
# 创建服务脚本 wcauto_service.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from wcauto import WeChat
import schedule
import time
from datetime import datetime

def scheduled_task():
    """定时任务示例"""
    wx = WeChat()
    message = f"定时任务测试 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    wx.SendMsg(message, "文件传输助手")

def main():
    """主函数"""
    print("微信自动化服务启动...")
    
    # 设置定时任务 - 每天上午9点执行
    schedule.every().day.at("09:00").do(scheduled_task)
    
    # 保持服务运行
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次

if __name__ == "__main__":
    main()
```

创建 Windows 任务计划程序任务：

1. 打开 "任务计划程序" (Task Scheduler)
2. 创建基本任务
3. 设置触发器（例如：系统启动时）
4. 设置操作为启动程序，选择打包后的可执行文件或 Python 脚本
5. 配置任务以最高权限运行

#### 3. 使用 Docker 部署 (高级)

虽然 wcauto 主要用于 Windows 环境，但可以通过 Windows 容器部署：

```dockerfile
# Dockerfile.windows
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# 安装 Python
RUN powershell -Command \
    $ProgressPreference = 'SilentlyContinue'; \
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe -OutFile python-installer.exe; \
    Start-Process python-installer.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait; \
    Remove-Item python-installer.exe

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . .

# 安装依赖
RUN pip install -r requirements.txt

# 设置入口点
CMD ["python", "wcauto_service.py"]
```

构建和运行容器：
```bash
# 构建镜像
docker build -f Dockerfile.windows -t wcauto .

# 运行容器
docker run -d --name wcauto-container wcauto
```

### 部署最佳实践

#### 1. 配置管理

创建配置文件 `config.ini`：

```ini
[wechat]
default_recipient = 文件传输助手
use_send_button = false
retry_count = 3
retry_interval = 2

[logging]
level = INFO
file_path = wcauto.log
max_size = 10485760  # 10MB
backup_count = 5

[schedule]
enabled = true
daily_time = 09:00
```

配置加载代码：

```python
import configparser
import os

def load_config(config_path="config.ini"):
    """加载配置文件"""
    config = configparser.ConfigParser()
    
    # 如果配置文件不存在，创建默认配置
    if not os.path.exists(config_path):
        config['wechat'] = {
            'default_recipient': '文件传输助手',
            'use_send_button': 'false',
            'retry_count': '3',
            'retry_interval': '2'
        }
        config['logging'] = {
            'level': 'INFO',
            'file_path': 'wcauto.log',
            'max_size': '10485760',
            'backup_count': '5'
        }
        config['schedule'] = {
            'enabled': 'true',
            'daily_time': '09:00'
        }
        
        with open(config_path, 'w') as f:
            config.write(f)
    
    config.read(config_path)
    return config
```

#### 2. 日志管理

实现日志轮转：

```python
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(config):
    """设置日志轮转"""
    log_path = config.get('logging', 'file_path', fallback='wcauto.log')
    max_size = config.getint('logging', 'max_size', fallback=10485760)
    backup_count = config.getint('logging', 'backup_count', fallback=5)
    level = config.get('logging', 'level', fallback='INFO')
    
    # 确保日志目录存在
    log_dir = os.path.dirname(log_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 创建日志记录器
    logger = logging.getLogger('wcauto')
    logger.setLevel(getattr(logging, level.upper()))
    
    # 创建文件处理器（带轮转）
    file_handler = RotatingFileHandler(
        log_path, 
        maxBytes=max_size, 
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setLevel(getattr(logging, level.upper()))
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加处理器到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
```

#### 3. 错误处理与恢复

实现自动恢复机制：

```python
import time
import subprocess
import sys

class WeChatAutomation:
    def __init__(self, config):
        self.config = config
        self.max_restarts = 3
        self.restart_count = 0
        self.last_error_time = None
    
    def restart_wechat_if_needed(self):
        """如果需要，重启微信"""
        current_time = time.time()
        
        # 如果距离上次错误不到5分钟，不重启
        if self.last_error_time and (current_time - self.last_error_time < 300):
            return False
        
        # 如果重启次数过多，不重启
        if self.restart_count >= self.max_restarts:
            return False
        
        try:
            # 终止微信进程
            subprocess.run(['taskkill', '/F', '/IM', 'WeChat.exe'], check=True)
            subprocess.run(['taskkill', '/F', '/IM', 'WeChatApp.exe'], check=True)
            
            # 等待进程完全终止
            time.sleep(3)
            
            # 启动微信
            wechat_path = os.path.join(os.environ['PROGRAMFILES(x86)'], 'Tencent', 'WeChat', 'WeChat.exe')
            if not os.path.exists(wechat_path):
                wechat_path = os.path.join(os.environ['PROGRAMW6432'], 'Tencent', 'WeChat', 'WeChat.exe')
            
            if os.path.exists(wechat_path):
                subprocess.Popen([wechat_path])
                self.restart_count += 1
                self.last_error_time = current_time
                return True
            else:
                print("找不到微信可执行文件")
                return False
        except Exception as e:
            print(f"重启微信失败: {e}")
            return False
    
    def safe_send_message(self, message, recipient=None):
        """安全发送消息，带自动恢复"""
        from wcauto import WeChat
        
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                wx = WeChat()
                
                # 检查微信是否运行
                if not wx.check_wechat_running():
                    print("微信未运行，尝试重启...")
                    if not self.restart_wechat_if_needed():
                        return False
                    time.sleep(10)  # 等待微信启动
                    continue
                
                # 激活微信窗口
                if not wx.activate_wechat():
                    print("无法激活微信窗口，尝试重启...")
                    if not self.restart_wechat_if_needed():
                        return False
                    time.sleep(10)  # 等待微信启动
                    continue
                
                # 发送消息
                if recipient is None:
                    recipient = self.config.get('wechat', 'default_recipient', fallback='文件传输助手')
                
                use_send_button = self.config.getboolean('wechat', 'use_send_button', fallback=False)
                result = wx.SendMsg(message, recipient, use_send_button)
                
                if result:
                    # 成功发送，重置重启计数
                    self.restart_count = 0
                    return True
                else:
                    print(f"消息发送失败 (尝试 {attempt + 1}/{max_attempts})")
                    if attempt < max_attempts - 1:
                        time.sleep(2)  # 等待后重试
            except Exception as e:
                print(f"发送消息异常 (尝试 {attempt + 1}/{max_attempts}): {e}")
                if attempt < max_attempts - 1:
                    time.sleep(2)  # 等待后重试
        
        return False
```

#### 4. 性能监控

实现性能监控：

```python
import psutil
import time
import threading

class PerformanceMonitor:
    def __init__(self, config):
        self.config = config
        self.running = False
        self.thread = None
        self.cpu_threshold = 80
        self.memory_threshold = 80
    
    def start(self):
        """启动性能监控"""
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop)
        self.thread.daemon = True
        self.thread.start()
        print("性能监控已启动")
    
    def stop(self):
        """停止性能监控"""
        self.running = False
        if self.thread:
            self.thread.join()
        print("性能监控已停止")
    
    def _monitor_loop(self):
        """监控循环"""
        while self.running:
            try:
                # 获取系统资源使用情况
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                # 检查是否超过阈值
                if cpu_percent > self.cpu_threshold or memory.percent > self.memory_threshold:
                    # 发送警告通知
                    wx = WeChat()
                    warning_msg = f"""
                    系统资源使用警告！
                    
                    CPU使用率: {cpu_percent}%
                    内存使用率: {memory.percent}%
                    
                    请检查系统状态。
                    """
                    wx.SendMsg(warning_msg, "系统管理员")
                
                # 等待一段时间再次检查
                time.sleep(300)  # 5分钟检查一次
            except Exception as e:
                print(f"性能监控异常: {e}")
                time.sleep(60)  # 出错后等待1分钟再试
```

#### 5. 部署脚本

创建自动化部署脚本 `deploy.py`：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import shutil
import configparser

def install_dependencies():
    """安装依赖"""
    print("正在安装依赖...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("依赖安装完成")

def create_config():
    """创建配置文件"""
    print("正在创建配置文件...")
    config = configparser.ConfigParser()
    
    config['wechat'] = {
        'default_recipient': '文件传输助手',
        'use_send_button': 'false',
        'retry_count': '3',
        'retry_interval': '2'
    }
    
    config['logging'] = {
        'level': 'INFO',
        'file_path': 'wcauto.log',
        'max_size': '10485760',
        'backup_count': '5'
    }
    
    config['schedule'] = {
        'enabled': 'true',
        'daily_time': '09:00'
    }
    
    with open('config.ini', 'w') as f:
        config.write(f)
    
    print("配置文件创建完成")

def create_executable():
    """创建可执行文件"""
    print("正在创建可执行文件...")
    
    # 检查 PyInstaller 是否已安装
    try:
        import PyInstaller
    except ImportError:
        print("正在安装 PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # 创建可执行文件
    subprocess.check_call([sys.executable, "-m", "PyInstaller", "--onefile", "--name", "wcauto_tool", "wcauto/wcauto.py"])
    
    # 移动可执行文件到项目根目录
    if os.path.exists("dist/wcauto_tool.exe"):
        shutil.move("dist/wcauto_tool.exe", ".")
        print("可执行文件创建完成: wcauto_tool.exe")
    else:
        print("可执行文件创建失败")

def create_service_script():
    """创建服务脚本"""
    print("正在创建服务脚本...")
    
    service_script = """import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from wcauto import WeChat
import schedule
import time
from datetime import datetime
import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def scheduled_task():
    config = load_config()
    wx = WeChat()
    recipient = config.get('wechat', 'default_recipient', fallback='文件传输助手')
    message = f"定时任务测试 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    wx.SendMsg(message, recipient)

def main():
    config = load_config()
    
    if config.getboolean('schedule', 'enabled', fallback=True):
        daily_time = config.get('schedule', 'daily_time', fallback='09:00')
        schedule.every().day.at(daily_time).do(scheduled_task)
        print(f"定时任务已设置，每天 {daily_time} 执行")
    
    print("微信自动化服务启动...")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
"""
    
    with open("wcauto_service.py", "w", encoding="utf-8") as f:
        f.write(service_script)
    
    print("服务脚本创建完成: wcauto_service.py")

def create_desktop_shortcut():
    """创建桌面快捷方式"""
    print("正在创建桌面快捷方式...")
    
    import win32com.client
    
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    path = os.path.join(desktop, 'wcauto_tool.lnk')
    
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = os.path.abspath("wcauto_tool.exe")
    shortcut.IconLocation = os.path.abspath("wcauto_tool.exe")
    shortcut.save()
    
    print("桌面快捷方式创建完成")

def main():
    """主函数"""
    print("开始部署 wcauto...")
    
    # 安装依赖
    install_dependencies()
    
    # 创建配置文件
    create_config()
    
    # 创建可执行文件
    create_executable()
    
    # 创建服务脚本
    create_service_script()
    
    # 创建桌面快捷方式
    try:
        create_desktop_shortcut()
    except Exception as e:
        print(f"创建桌面快捷方式失败: {e}")
    
    print("部署完成！")
    print("你可以:")
    print("1. 直接运行 wcauto_tool.exe 进行测试")
    print("2. 运行 wcauto_service.py 启动服务")
    print("3. 编辑 config.ini 自定义配置")

if __name__ == "__main__":
    main()
```

运行部署脚本：
```bash
python deploy.py
```

### 部署验证

创建验证脚本 `verify_deployment.py`：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import configparser

def verify_dependencies():
    """验证依赖是否安装正确"""
    print("验证依赖...")
    
    required_packages = [
        'pyautogui',
        'pyperclip',
        'uiautomation',
        'psutil',
        'pywin32'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} 已安装")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} 未安装")
    
    if missing_packages:
        print(f"缺少以下依赖: {', '.join(missing_packages)}")
        return False
    
    print("所有依赖已正确安装")
    return True

def verify_config():
    """验证配置文件"""
    print("验证配置文件...")
    
    if not os.path.exists('config.ini'):
        print("❌ 配置文件不存在")
        return False
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    required_sections = ['wechat', 'logging', 'schedule']
    for section in required_sections:
        if not config.has_section(section):
            print(f"❌ 配置文件缺少 [{section}] 部分")
            return False
    
    print("✅ 配置文件验证通过")
    return True

def verify_executable():
    """验证可执行文件"""
    print("验证可执行文件...")
    
    if os.path.exists('wcauto_tool.exe'):
        print("✅ 可执行文件存在")
        return True
    else:
        print("❌ 可执行文件不存在")
        return False

def verify_wechat():
    """验证微信是否可访问"""
    print("验证微信...")
    
    try:
        from wcauto import WeChat
        wx = WeChat()
        
        if wx.check_wechat_running():
            print("✅ 微信正在运行")
            return True
        else:
            print("❌ 微信未运行")
            return False
    except Exception as e:
        print(f"❌ 验证微信时出错: {e}")
        return False

def test_message_sending():
    """测试消息发送"""
    print("测试消息发送...")
    
    try:
        from wcauto import WeChat
        wx = WeChat()
        
        config = configparser.ConfigParser()
        config.read('config.ini')
        recipient = config.get('wechat', 'default_recipient', fallback='文件传输助手')
        
        result = wx.SendMsg("部署验证测试消息", recipient)
        
        if result:
            print("✅ 消息发送测试通过")
            return True
        else:
            print("❌ 消息发送测试失败")
            return False
    except Exception as e:
        print(f"❌ 消息发送测试出错: {e}")
        return False

def main():
    """主函数"""
    print("开始验证部署...")
    
    checks = [
        ("依赖验证", verify_dependencies),
        ("配置验证", verify_config),
        ("可执行文件验证", verify_executable),
        ("微信验证", verify_wechat),
        ("消息发送验证", test_message_sending)
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n--- {name} ---")
        result = check_func()
        results.append((name, result))
    
    print("\n--- 验证结果汇总 ---")
    all_passed = True
    for name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n🎉 所有验证通过！部署成功！")
        return 0
    else:
        print("\n⚠️ 部分验证失败，请检查上述问题")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

运行验证脚本：
```bash
python verify_deployment.py
```

## 🔧 API 文档

### WeChat 类

#### `__init__()`
初始化微信自动化实例。

#### `SendMsg(message, who=None, use_send_button=False)`
向指定联系人发送消息。

**参数：**
- `message` (str): 要发送的消息内容
- `who` (str, optional): 联系人名称，如果为None则发送到当前聊天
- `use_send_button` (bool, optional): 是否使用发送按钮（默认使用回车键）

**返回值：**
- `bool`: 发送成功返回 True，失败返回 False

#### `SendFiles(filepath, who=None)`
向指定联系人发送文件。

**参数：**
- `filepath` (str): 要发送的文件路径
- `who` (str, optional): 联系人名称，如果为None则发送到当前聊天

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

## ❓ 常见问题 (FAQ)

### 基础问题

**Q: 消息发送失败怎么办？**
A: 
- 检查微信是否已启动并登录
- 确认联系人名称正确
- 尝试使用 `use_send_button=True` 参数
- 检查程序是否以管理员权限运行
- 确保微信窗口可见且未被遮挡

**Q: 文件发送失败怎么办？**
A:
- 确认文件路径正确且文件存在
- 检查文件大小是否超过微信限制（通常100MB以内）
- 确认联系人名称正确
- 检查程序是否以管理员权限运行
- 确保文件类型不被微信限制

**Q: 如何提高发送成功率？**
A:
- 确保微信窗口可见且未被遮挡
- 适当增加操作之间的等待时间
- 使用最新版本的微信
- 避免在发送过程中操作鼠标键盘
- 使用 `use_send_button=True` 参数

**Q: 支持群聊消息发送吗？**
A: 是的，只需将群聊名称作为 `who` 参数传入即可。

### 技术问题

**Q: 程序提示"无法找到微信窗口"怎么办？**
A:
- 确保微信已启动并登录
- 检查微信窗口是否最小化到系统托盘
- 尝试重启微信
- 确认程序以管理员权限运行

**Q: 坐标计算不准确怎么办？**
A:
- 不同微信版本可能需要调整坐标计算
- 检查屏幕分辨率设置
- 尝试调整微信窗口大小和位置
- 查看项目Wiki中的坐标校准指南

**Q: 如何调试程序运行问题？**
A:
- 启用详细日志记录
- 检查 `wcauto.log` 文件
- 使用调试模式运行程序
- 查看项目Issues中是否有类似问题

### 部署问题

**Q: 依赖安装失败怎么办？**
A:
- 检查Python版本（需要3.8+）
- 尝试使用国内镜像源：`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`
- 确保网络连接正常
- 查看详细的错误信息

**Q: 打包后的程序无法运行怎么办？**
A:
- 检查是否缺少必要的依赖库
- 尝试重新打包
- 使用源码方式运行测试
- 查看打包日志中的警告信息

**Q: 如何配置定时任务？**
A:
- 编辑 `config.ini` 文件中的 `schedule` 部分
- 使用Windows任务计划程序
- 参考部署指南中的详细说明
- 查看项目Wiki中的定时任务配置教程

### 安全与合规

**Q: 使用这个工具安全吗？**
A:
- 本项目完全开源，代码透明可审查
- 不收集任何用户数据
- 仅操作微信界面，不涉及微信内部数据
- 请遵守微信使用条款，避免滥用

**Q: 会被微信检测为异常行为吗？**
A:
- 合理使用通常不会被检测
- 避免频繁、大批量发送消息
- 建议用于个人自动化需求
- 不要用于商业营销等违规用途

## 🚀 部署教程

### 快速部署（推荐）

使用我们提供的自动化部署脚本，一键完成所有配置：

```bash
# 克隆项目
git clone https://github.com/YangShengzhou03/wcauto.git
cd wcauto

# 运行自动化部署脚本
python deploy.py
```

部署脚本将自动完成以下操作：
- 安装所有必要的依赖包
- 创建默认配置文件
- 打包为可执行文件
- 创建服务脚本
- 生成桌面快捷方式

### 手动部署

如果您需要自定义配置，可以按照以下步骤手动部署：

#### 1. 环境准备

**系统要求：**
- Windows 10/11 (64位)
- Python 3.8 或更高版本
- 微信桌面版 (已登录)

**Python 环境配置：**
```bash
# 检查 Python 版本
python --version

# 如果未安装 Python，请从 https://www.python.org/downloads/ 下载安装
```

#### 2. 项目设置

```bash
# 克隆项目
git clone https://github.com/YangShengzhou03/wcauto.git
cd wcauto

# 创建虚拟环境 (推荐)
python -m venv venv

# 激活虚拟环境
# Windows CMD:
venv\Scripts\activate.bat
# Windows PowerShell:
venv\Scripts\Activate.ps1

# 安装依赖
pip install -r requirements.txt
```

#### 3. 配置管理

创建配置文件 `config.ini`：

```ini
[wechat]
default_recipient = 文件传输助手
use_send_button = false
retry_count = 3
retry_interval = 2

[logging]
level = INFO
file_path = wcauto.log
max_size = 10485760  # 10MB
backup_count = 5

[schedule]
enabled = true
daily_time = 09:00
```

#### 4. 测试部署

运行验证脚本检查部署是否成功：

```bash
python verify_deployment.py
```

### 生产环境部署

#### 1. 打包为可执行文件

使用 PyInstaller 将项目打包为独立的可执行文件：

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包为单个可执行文件
pyinstaller --onefile --name wcauto_tool wcauto/wcauto.py
```

#### 2. 创建系统服务

使用 Windows 任务计划程序创建定时任务：

1. 打开 "任务计划程序" (Task Scheduler)
2. 创建基本任务
3. 设置触发器（例如：系统启动时）
4. 设置操作为启动程序，选择打包后的可执行文件
5. 配置任务以最高权限运行

#### 3. 使用 Docker 部署 (高级)

虽然 wcauto 主要用于 Windows 环境，但可以通过 Windows 容器部署：

```dockerfile
# Dockerfile.windows
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# 安装 Python
RUN powershell -Command \
    $ProgressPreference = 'SilentlyContinue'; \
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe -OutFile python-installer.exe; \
    Start-Process python-installer.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait; \
    Remove-Item python-installer.exe

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . .

# 安装依赖
RUN pip install -r requirements.txt

# 设置入口点
CMD ["python", "wcauto_service.py"]
```

### 部署最佳实践

#### 1. 监控与日志

- 启用日志轮转功能
- 定期检查日志文件
- 设置性能监控
- 配置错误告警

#### 2. 备份策略

- 定期备份配置文件
- 保存重要日志
- 备份自定义脚本

#### 3. 安全考虑

- 使用虚拟环境
- 定期更新依赖
- 限制程序权限
- 监控异常行为

## 🐛 问题反馈

如果您在使用过程中遇到问题，请通过以下方式反馈：

### GitHub Issues
[![GitHub Issues](https://img.shields.io/github/issues/YangShengzhou03/wcauto?style=for-the-badge)](https://github.com/YangShengzhou03/wcauto/issues)

- 报告Bug或问题
- 提出功能建议
- 讨论技术实现

### 项目Wiki
[![Documentation](https://img.shields.io/badge/docs-wiki-blue?style=for-the-badge)](https://github.com/YangShengzhou03/wcauto/wiki)

- 详细的使用教程
- 技术文档和API参考
- 常见问题解答
- 最佳实践指南

### 反馈模板

为了高效解决问题，请按照以下模板提交反馈：

```markdown
## 问题描述
[清晰描述遇到的问题]

## 环境信息
- 操作系统：Windows 10/11
- Python版本：3.8.10
- 微信版本：3.9.x
- wcauto版本：[填写版本号]

## 重现步骤
1. [步骤1]
2. [步骤2]
3. [步骤3]

## 期望行为
[描述期望的正常行为]

## 实际行为
[描述实际发生的错误行为]

## 错误日志
[粘贴相关的错误日志]

## 附加信息
[其他相关信息或截图]
```

## 🏗️ 架构设计

### 系统架构

wcauto 采用模块化设计，主要包含以下核心组件：

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   用户接口层     │    │   业务逻辑层     │    │   底层驱动层     │
│                 │    │                 │    │                 │
│ • API接口       │◄──►│ • 消息发送逻辑   │◄──►│ • 窗口操作      │
│ • 配置管理      │    │ • 文件传输逻辑   │    │ • 键盘模拟      │
│ • 日志记录      │    │ • 异常处理      │    │ • 鼠标控制      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 核心算法

#### 1. 窗口查找算法
```python
def find_wechat_window():
    """查找微信窗口的优化算法"""
    # 使用多条件匹配策略
    # 1. 窗口标题匹配
    # 2. 进程名验证
    # 3. 窗口类名检查
    # 4. 坐标位置验证
```

#### 2. 消息发送算法
```python
def send_message_algorithm():
    """消息发送的核心算法"""
    # 1. 激活目标窗口
    # 2. 定位输入框
    # 3. 清空现有内容
    # 4. 输入消息文本
    # 5. 选择发送方式
    # 6. 验证发送结果
```

#### 3. 文件传输算法
```python
def file_transfer_algorithm():
    """文件传输的核心算法"""
    # 1. 定位文件按钮
    # 2. 选择文件路径
    # 3. 等待文件上传
    # 4. 确认发送操作
    # 5. 验证传输结果
```

### 性能优化

#### 1. 缓存机制
- 窗口句柄缓存
- 坐标位置缓存
- 联系人列表缓存

#### 2. 异步处理
- 非阻塞窗口操作
- 并行消息处理
- 后台文件传输

#### 3. 资源管理
- 内存优化
- 进程监控
- 异常恢复

### 扩展性设计

#### 1. 插件系统
支持通过插件扩展功能：
- 消息模板插件
- 定时任务插件
- 监控告警插件

#### 2. 配置驱动
所有行为通过配置文件控制：
- 窗口查找策略
- 发送间隔设置
- 重试机制配置

#### 3. 接口抽象
提供统一的接口层：
- 消息发送接口
- 文件传输接口
- 状态查询接口

## 🤝 参与贡献

我们非常欢迎社区贡献！无论是报告bug、提出新功能建议，还是提交代码改进，都是对项目的宝贵支持。

### 贡献指南

#### 1. 报告问题
- 使用 [GitHub Issues](https://github.com/YangShengzhou03/wcauto/issues) 报告bug
- 提供详细的重现步骤和环境信息
- 包含相关的错误日志和截图

#### 2. 功能建议
- 在 Issues 中描述新功能需求
- 说明使用场景和预期效果
- 讨论技术实现方案

#### 3. 代码贡献

**开发环境设置：**
```bash
# 1. Fork 项目
# 2. 克隆你的 Fork
git clone https://github.com/your-username/wcauto.git
cd wcauto

# 3. 创建开发分支
git checkout -b feature/your-feature-name

# 4. 安装开发依赖
pip install -r requirements-dev.txt

# 5. 运行测试
python -m pytest tests/
```

**代码规范：**
- 遵循 PEP 8 代码风格
- 添加适当的注释和文档
- 编写单元测试覆盖新功能
- 确保所有测试通过

**提交 Pull Request：**
```bash
# 1. 提交更改
git add .
git commit -m "feat: 添加新功能描述"

# 2. 推送到你的分支
git push origin feature/your-feature-name

# 3. 在 GitHub 创建 Pull Request
```

### 贡献类型

#### 🐛 Bug 修复
- 修复已知问题
- 改进错误处理
- 增强稳定性

#### ✨ 新功能
- 添加新特性
- 扩展API接口
- 改进用户体验

#### 📚 文档改进
- 完善使用文档
- 添加代码注释
- 翻译多语言文档

#### 🔧 性能优化
- 优化算法效率
- 减少资源占用
- 改进响应速度

#### 🧪 测试覆盖
- 添加单元测试
- 集成测试
- 性能测试

### 社区准则

1. **尊重他人**：保持友好和专业的交流氛围
2. **建设性反馈**：提供具体、有帮助的反馈
3. **包容性**：欢迎不同背景和技能水平的贡献者
4. **遵守规范**：遵循项目代码规范和贡献流程

## 👥 贡献者

感谢所有为这个项目做出贡献的开发者！

### 核心贡献者

[![Contributors](https://contrib.rocks/image?repo=YangShengzhou03/wcauto)](https://github.com/YangShengzhou03/wcauto/graphs/contributors)

### 特别感谢

感谢以下开发者的宝贵贡献：
[![Contributors](https://contrib.rocks/image?repo=YangShengzhou03/wcauto)](https://github.com/YangShengzhou03/wcauto/graphs/contributors)

### 成为贡献者

想要加入贡献者行列？请参考 [贡献指南](#参与贡献) 开始你的第一次贡献！

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
FITNESS FOR A PARTICULAR PURPOSE AND NONINGRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">
  <sub>Built with ❤️ using Python and automation technologies</sub>
  <br>
  <sub>感谢所有贡献者和用户的支持！</sub>
</div>