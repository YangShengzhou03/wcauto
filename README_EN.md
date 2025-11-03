<div align="center">
  <h1>wcauto - WeChat Automation Tool</h1>
  
  <p>
    <em>A Python-based automation library for WeChat Desktop, supporting message sending, file transfer, window control, and more</em>
  </p>

  <div>
    <!-- Project Status -->
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
    <a href="https://github.com/YangShengzhou03/wcauto/actions">
      <img src="https://img.shields.io/github/actions/workflow/status/YangShengzhou03/wcauto/ci.yml?style=for-the-badge&logo=github-actions&label=CI/CD" alt="CI/CD Status">
    </a>
  </div>

  <br />

  <div>
    <!-- Tech Stack -->
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" alt="Python Version">
    </a>
    <a href="https://pyautogui.readthedocs.io/">
      <img src="https://img.shields.io/badge/PyAutoGUI-0.9.54-green?style=for-the-badge&logo=python" alt="PyAutoGUI Version">
    </a>
    <a href="https://github.com/yinkaisheng/Python-UIAutomation-for-Windows">
      <img src="https://img.shields.io/badge/UIAutomation-2.0.19-orange?style=for-the-badge&logo=windows" alt="UIAutomation Version">
    </a>
    <a href="https://pypi.org/project/pyperclip/">
      <img src="https://img.shields.io/badge/Pyperclip-1.8.2-yellow?style=for-the-badge&logo=python" alt="Pyperclip Version">
    </a>
    <a href="https://pypi.org/project/pywin32/">
      <img src="https://img.shields.io/badge/pywin32-306-red?style=for-the-badge&logo=windows" alt="pywin32 Version">
    </a>
  </div>

  <br />
  
  [![Star History Chart](https://api.star-history.com/svg?repos=YangShengzhou03/wcauto&type=Date)](https://star-history.com/#YangShengzhou03/wcauto&Date)

  <br />
  
  <div>
    <a href="README.md">中文</a> | 
    <a href="#-quick-start">Quick Start</a> | 
    <a href="#-api-documentation">API Documentation</a> | 
    <a href="#-faq">FAQ</a>
  </div>

</div>

## 📖 Table of Contents

- [✨ Project Overview](#-project-overview)
- [🚀 Core Features](#-core-features)
- [📦 Quick Start](#-quick-start)
- [🔧 Installation Guide](#-installation-guide)
- [💡 Usage Tutorial](#-usage-tutorial)
- [📚 API Documentation](#-api-documentation)
- [🏗️ Architecture Design](#️-architecture-design)
- [🔍 FAQ](#-faq)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## ✨ Project Overview

**wcauto** is a Python-based automation library specifically designed for WeChat Desktop on Windows platform. It simulates user operations to achieve automated message sending, file transfer, window control, and more.

### 💡 Use Cases

| Category | Specific Applications | Key Features |
|----------|----------------------|--------------|
| **Automated Notifications** | System monitoring, scheduled reminders | Real-time response, precise delivery |
| **Batch Operations** | Marketing campaigns, group messaging | Efficient batch processing, intelligent scheduling |
| **File Transfer** | File backup, document synchronization | Stable and reliable, supports large files |
| **Scheduled Tasks** | Calendar scheduling, task reminders | Precise timing, automatic execution |
| **Bot Development** | Smart customer service, auto-reply | Flexible extension, intelligent interaction |
| **Automated Testing** | WeChat functionality testing | Comprehensive coverage, continuous integration |

### 🎯 Design Philosophy

- **Easy to Use**: Intuitive API interface, low learning curve
- **Stable and Reliable**: Multiple exception handling mechanisms, ensuring operation success rate
- **Flexible Extension**: Modular design, supports custom function extensions
- **Performance Optimized**: Smart caching and resource management, improved execution efficiency
- **Security Compliant**: Follows WeChat usage guidelines, ensures compliant operations

## 🚀 Core Features

### 🔧 Core Functionality

#### WeChat Window Management
- **Smart Window Detection**: Automatically finds and activates WeChat windows
- **Window Status Monitoring**: Real-time monitoring of window status changes
- **Multi-Window Support**: Supports switching between multiple WeChat windows

#### Message Operations
- **Text Message Sending**: Supports sending text messages to specified contacts
- **Message Status Verification**: Automatically verifies message sending status
- **Sending Method Selection**: Supports both Enter key and Send button methods

#### File Transfer
- **File Sending Function**: Supports sending files to specified contacts
- **File Type Support**: Supports common document, image, archive formats
- **Transfer Status Monitoring**: Real-time monitoring of file transfer progress

#### System Integration
- **Process Detection**: Checks if WeChat is running
- **Exception Handling**: Multiple exception handling mechanisms for improved stability
- **Resource Management**: Smart resource release and memory management

### 🛠️ Technical Features

#### Automation Technology
- **Multi-Solution Compatibility**: Provides primary and backup solutions for higher success rate
- **Smart Coordinate Calculation**: Automatically calculates click positions based on window size
- **Clipboard Operations**: Uses clipboard for text transfer
- **Hotkey Simulation**: Supports various keyboard shortcut operations

#### Stability Assurance
- **Retry Mechanism**: Automatic retry for failed operations
- **Timeout Control**: Reasonable timeout settings for operations
- **Error Recovery**: Smart error detection and automatic recovery

#### Performance Optimization
- **Asynchronous Operations**: Supports asynchronous execution for improved efficiency
- **Resource Reuse**: Smart caching and connection reuse
- **Memory Optimization**: Optimized memory usage, reduced resource consumption

## 📦 Quick Start

### 5-Minute Quick Start

#### 1. Environment Preparation
Ensure your system meets the following requirements:
- **Operating System**: Windows 10/11 (64-bit)
- **Python Version**: 3.8 or higher (recommended 3.9+)
- **WeChat Version**: WeChat Desktop (logged in and running)

#### 2. Install wcauto

**Method 1: Install from GitHub (Recommended)**
```bash
# Install latest version
pip install git+https://github.com/YangShengzhou03/wcauto.git

# Or install specific version
pip install wcauto==1.0.0
```

**Method 2: Source Installation (Development Mode)**
```bash
# Clone the project
git clone https://github.com/YangShengzhou03/wcauto.git
cd wcauto

# Install production dependencies
pip install -r requirements.txt

# Development mode installation
pip install -e .
```

**Method 3: Install Core Dependencies Only**
```bash
# If you only need core functionality, install dependencies manually
pip install pyautogui==0.9.54 pyperclip==1.8.2 uiautomation==2.0.19 psutil==5.9.5 pywin32==306
```

#### 3. Basic Usage Example

```python
from wcauto import WeChat

# Create WeChat automation instance
wx = WeChat()

# Check if WeChat is running
if not wx.check_wechat_running():
    print("⚠️ WeChat is not running, please start WeChat first")
    exit(1)

# Send message to File Transfer Assistant
result = wx.send_msg("Hello, this is a test message!", "File Transfer Assistant")

if result:
    print("✅ Message sent successfully!")
else:
    print("❌ Message sending failed!")
```

#### 4. File Sending Example

```python
from wcauto import WeChat

# Initialize WeChat automation instance
wx = WeChat()

# Send file
result = wx.send_files(r"C:\path\to\file.pdf", "File Transfer Assistant")

if result:
    print("✅ File sent successfully!")
else:
    print("❌ File sending failed!")
```

### Complete Feature Demo

```python
from wcauto import WeChat
import time

def comprehensive_demo():
    """Complete feature demonstration"""
    wx = WeChat()
    
    # Check WeChat running status
    if not wx.check_wechat_running():
        print("⚠️ WeChat is not running, please start WeChat first")
        return
    
    print("✅ WeChat is running")
    
    # Activate WeChat window
    if wx.activate_wechat():
        print("✅ WeChat window activated successfully")
    else:
        print("❌ WeChat window activation failed")
        return
    
    # Send text message
    result1 = wx.send_msg("First test message", "File Transfer Assistant")
    print(f"📨 Message sending result: {'Success' if result1 else 'Failed'}")
    
    time.sleep(1)  # Wait 1 second
    
    # Send message using send button
    result2 = wx.send_msg("Message using send button", "File Transfer Assistant", use_send_button=True)
    print(f"📨 Send button message result: {'Success' if result2 else 'Failed'}")
    
    # Send file
    # result3 = wx.send_files(r"C:\path\to\test.pdf", "File Transfer Assistant")
    # print(f"📎 File sending result: {'Success' if result3 else 'Failed'}")

if __name__ == "__main__":
    comprehensive_demo()
```

## 🔧 Installation Guide

### System Requirements

| Component | Minimum Requirements | Recommended Configuration | Notes |
|-----------|---------------------|--------------------------|-------|
| **Operating System** | Windows 10 | Windows 11 | Windows platform only |
| **Python** | 3.8 | 3.9+ | Python environment required |
| **WeChat Version** | WeChat Desktop | Latest version | Must be installed and logged in |
| **Memory** | 4GB | 8GB+ | Ensure smooth system operation |
| **Screen Resolution** | 1366×768 | 1920×1080+ | Ensure UI elements display correctly |

### Installation Methods

#### Method 1: pip Installation (Recommended)

```bash
# Install from GitHub
pip install git+https://github.com/YangShengzhou03/wcauto.git

# Or install specific version
pip install wcauto==1.0.0
```

#### Method 2: Source Installation (Development Mode)

```bash
# Clone the project
git clone https://github.com/YangShengzhou03/wcauto.git
cd wcauto

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows CMD:
venv\Scripts\activate.bat
# Windows PowerShell:
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Development mode installation
pip install -e .
```

#### Method 3: Docker Installation (Advanced)

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "-c", "from wcauto import WeChat; wx = WeChat(); print('wcauto installed successfully!')]"]
```

### Dependency Information

wcauto depends on the following Python packages:

| Package | Version Requirement | Main Function | Official Documentation |
|---------|---------------------|---------------|------------------------|
| `pyautogui` | >=0.9.53,<1.0.0 | Mouse/keyboard automation control | [Docs](https://pyautogui.readthedocs.io/) |
| `pyperclip` | >=1.8.2,<2.0.0 | Cross-platform clipboard operations | [Docs](https://pypi.org/project/pyperclip/) |
| `uiautomation` | >=2.0.15,<3.0.0 | Windows UI automation | [Docs](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows) |
| `psutil` | >=5.8.0,<6.0.0 | Process management | [Docs](https://psutil.readthedocs.io/) |
| `pywin32` | >=300,<310 | Windows API interface | [Docs](https://pypi.org/project/pywin32/) |

### Installation Verification

Create verification script `verify_installation.py`:

```python
#!/usr/bin/env python3
"""
wcauto installation verification script
Used to verify if wcauto is correctly installed and configured
"""

import sys
import importlib.util

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python version check passed: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python version too low: {version.major}.{version.minor}.{version.micro}, requires 3.8+")
        return False

def check_dependencies():
    """Check if dependencies are installed"""
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
                print(f"✅ {package} installed")
            else:
                print(f"❌ {package} not installed")
                all_installed = False
        except ImportError:
            print(f"❌ {package} import failed")
            all_installed = False
    
    return all_installed

def check_wcauto_import():
    """Check if wcauto can be imported normally"""
    try:
        from wcauto import WeChat
        print("✅ wcauto import successful")
        return True
    except ImportError as e:
        print(f"❌ wcauto import failed: {e}")
        return False

def main():
    """Main verification function"""
    print("🚀 Starting wcauto installation verification...")
    print("=" * 50)
    
    # Check Python version
    python_ok = check_python_version()
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    # Check wcauto import
    import_ok = check_wcauto_import()
    
    print("=" * 50)
    
    if python_ok and deps_ok and import_ok:
        print("🎉 All checks passed! wcauto installation successful!")
        print("💡 You can now start using wcauto for WeChat automation")
        return True
    else:
        print("❌ Installation verification failed, please check the above error messages")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
```

Run verification script:

```bash
python verify_installation.py
```

## 💡 Usage Tutorial

### Basic Operations

#### 1. Initialization and Basic Checks

```python
from wcauto import WeChat

# Create WeChat automation instance
wx = WeChat()

# Check if WeChat is running
if not wx.check_wechat_running():
    print("WeChat is not running, please start WeChat first")
    exit(1)

# Activate WeChat window
if not wx.activate_wechat():
    print("Unable to activate WeChat window")
    exit(1)
```

#### 2. Sending Text Messages

```python
# Send to current chat window
wx.send_msg("This is a test message")

# Send to specified contact
wx.send_msg("Hello, this is a test message!", "File Transfer Assistant")

# Use send button instead of Enter key
wx.send_msg("Message using send button", "Contact Name", use_send_button=True)
```

#### 3. Sending Files

```python
# Send single file
file_path = r"C:\path\to\file.pdf"
result = wx.send_files(file_path, "File Transfer Assistant")

if result:
    print("File sent successfully!")
else:
    print("File sending failed!")

# Send to current chat
wx.send_files(r"C:\path\to\image.jpg")
```

### Advanced Applications

#### 1. Batch Message Sending

```python
import time

def send_batch_messages(recipient, messages, delay=1):
    """
    Send batch messages to specified contact
    
    Args:
        recipient (str): Recipient name
        messages (list): List of messages
        delay (int): Sending interval (seconds)
    """
    wx = WeChat()
    
    if not wx.check_wechat_running():
        print("WeChat is not running, please start WeChat first")
        return False
    
    success_count = 0
    total_count = len(messages)
    
    for i, msg in enumerate(messages, 1):
        print(f"Sending message {i}/{total_count}...")
        
        if wx.send_msg(msg, recipient):
            success_count += 1
            print(f"✅ Message sent successfully: {msg[:20]}...")
        else:
            print(f"❌ Message sending failed: {msg[:20]}...")
        
        # Avoid sending too fast
        if i < total_count:
            time.sleep(delay)
    
    success_rate = (success_count / total_count) * 100
    print(f"📊 Batch sending completed: {success_count}/{total_count} successful ({success_rate:.1f}%)")
    return success_count == total_count

# Usage example
messages = [
    "This is the first message",
    "This is the second message", 
    "This is the third message",
    "This is the fourth message",
    "This is the fifth message"
]

send_batch_messages("File Transfer Assistant", messages, delay=2)
```

#### 2. Scheduled Message Sending

```python
import schedule
import time
from datetime import datetime

def send_scheduled_message(recipient, message, schedule_time):
    """
    Send scheduled message
    
    Args:
        recipient (str): Recipient name
        message (str): Message content
        schedule_time (str): Scheduled time, format "HH:MM"
    """
    def job():
        wx = WeChat()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if wx.send_msg(message, recipient):
            print(f"{timestamp} - ✅ Scheduled message sent successfully")
        else:
            print(f"{timestamp} - ❌ Scheduled message sending failed")
    
    schedule.every().day.at(schedule_time).do(job)
    print(f"⏰ Scheduled message set: {schedule_time} to {recipient}")
    
    # Keep scheduler running
    while True:
        schedule.run_pending()
        time.sleep(1)

# Usage example (uncomment to enable)
# send_scheduled_message("File Transfer Assistant", "This is a scheduled message", "14:30")
```

#### 3. Batch File Sending

```python
import os
import time

def send_batch_files(recipient, file_paths, delay=2):
    """
    Send batch files to specified contact
    
    Args:
        recipient (str): Recipient name
        file_paths (list): List of file paths
        delay (int): Sending interval (seconds)
    """
    wx = WeChat()
    
    if not wx.check_wechat_running():
        print("WeChat is not running, please start WeChat first")
        return False
    
    success_count = 0
    total_count = len(file_paths)
    
    for i, file_path in enumerate(file_paths, 1):
        filename = os.path.basename(file_path)
        print(f"Sending file {i}/{total_count}: {filename}")
        
        if not os.path.exists(file_path):
            print(f"❌ File does not exist: {file_path}")
            continue
        
        if wx.send_files(file_path, recipient):
            success_count += 1
            print(f"✅ File sent successfully: {filename}")
        else:
            print(f"❌ File sending failed: {filename}")
        
        # Avoid sending too fast
        if i < total_count:
            time.sleep(delay)
    
    success_rate = (success_count / total_count) * 100
    print(f"📊 Batch sending completed: {success_count}/{total_count} successful ({success_rate:.1f}%)")
    return success_count > 0

# Usage example
files = [
    r"C:\path\to\file1.pdf",
    r"C:\path\to\file2.jpg", 
    r"C:\path\to\file3.docx"
]

send_batch_files("File Transfer Assistant", files, delay=3)
```

#### 4. Message Sending with Retry Mechanism

```python
def send_with_retry(message, recipient, max_retries=3, retry_delay=2):
    """
    Send message with retry mechanism
    
    Args:
        message (str): Message content
        recipient (str): Recipient name
        max_retries (int): Maximum retry attempts
        retry_delay (int): Retry interval (seconds)
    """
    wx = WeChat()
    
    for attempt in range(max_retries):
        try:
            print(f"🔄 Attempting to send message (attempt {attempt + 1}/{max_retries})...")
            
            if wx.send_msg(message, recipient):
                print(f"✅ Message sent successfully (attempt {attempt + 1}/{max_retries})")
                return True
            else:
                print(f"❌ Message sending failed (attempt {attempt + 1}/{max_retries})")
                
        except Exception as e:
            print(f"⚠️ Sending exception (attempt {attempt + 1}/{max_retries}): {e}")
        
        # If not the last attempt, wait and retry
        if attempt < max_retries - 1:
            print(f"⏳ Waiting {retry_delay} seconds before retry...")
            time.sleep(retry_delay)
    
    print(f"💥 Message sending failed, reached maximum retry attempts {max_retries}")
    return False

# Usage example
send_with_retry("This is an important test message", "File Transfer Assistant", max_retries=3)
```

#### 5. Custom Logging Configuration

```python
import logging

def setup_custom_logger(log_file='wcauto.log', level=logging.INFO):
    """
    Set up custom logging configuration
    
    Args:
        log_file (str): Log file path
        level: Logging level
    """
    # Create logger
    logger = logging.getLogger('wcauto')
    logger.setLevel(level)
    
    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger
    
    # Create file handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(level)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Usage example
logger = setup_custom_logger()
wx = WeChat()
logger.info("WeChat automation instance created")
```

### Practical Application Scenarios

#### 1. Automated Daily Report Sending

```python
import datetime

def send_daily_report(recipient="Supervisor"):
    """Send daily work report"""
    # Generate report content
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report_content = f"""
📊 Daily Work Report - {today}

✅ Today's Completed Work:
1. Completed requirements analysis for Project A
2. Fixed 3 critical bugs
3. Participated in team technical sharing meeting
4. Code review and optimization

📅 Tomorrow's Plan:
1. Start core functionality development for Project B
2. Conduct system performance testing
3. Write technical documentation

💡 Issues and Suggestions:
- Suggest optimizing development environment configuration
- Need more testing resource support

Thank you for reviewing!
    """
    
    # Send report
    wx = WeChat()
    if wx.send_msg(report_content, recipient):
        print("✅ Report sent successfully")
        return True
    else:
        print("❌ Report sending failed")
        return False

# Send daily report at 6 PM every day
# schedule.every().day.at("18:00").do(send_daily_report)
```

## 📚 API Documentation

### WeChat Class

#### Constructor
```python
WeChat()
```
Creates a new WeChat automation instance.

#### Methods

##### `check_wechat_running()`
Checks if WeChat process is running.

**Returns:**
- `bool`: True if WeChat is running, False otherwise

##### `activate_wechat()`
Activates the WeChat window and brings it to foreground.

**Returns:**
- `bool`: True if activation successful, False otherwise

##### `send_msg(message, recipient=None, use_send_button=False)`
Sends a text message to specified recipient.

**Parameters:**
- `message` (str): The message content to send
- `recipient` (str, optional): Recipient name. If None, sends to current chat
- `use_send_button` (bool): Whether to use send button instead of Enter key

**Returns:**
- `bool`: True if message sent successfully, False otherwise

##### `send_files(file_path, recipient=None)`
Sends a file to specified recipient.

**Parameters:**
- `file_path` (str): Path to the file to send
- `recipient` (str, optional): Recipient name. If None, sends to current chat

**Returns:**
- `bool`: True if file sent successfully, False otherwise

## 🔍 FAQ

### Q: Why can't wcauto find the WeChat window?
**A:** Make sure:
1. WeChat Desktop is running and logged in
2. The WeChat window is not minimized to system tray
3. Your screen resolution is at least 1366×768
4. You're running the script as administrator (if required by your system)

### Q: Why does message sending sometimes fail?
**A:** Common reasons include:
1. WeChat window lost focus during operation
2. Network connection issues
3. WeChat anti-automation detection
4. Insufficient delay between operations

### Q: Is wcauto safe to use?
**A:** wcauto is designed to be safe when used responsibly:
1. Follows WeChat's terms of service
2. Uses human-like timing to avoid detection
3. Includes proper error handling
4. Does not modify WeChat's internal data

### Q: Can I use wcauto on macOS or Linux?
**A:** Currently, wcauto only supports Windows due to its dependency on Windows-specific automation libraries.

### Q: How to handle WeChat updates?
**A:** WeChat updates may break automation functionality. Monitor the project's GitHub repository for updates and compatibility information.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/wcauto.git`
3. Install development dependencies: `pip install -r requirements-dev.txt`
4. Make your changes
5. Run tests: `pytest tests/`
6. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for all public functions
- Include tests for new functionality

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>
    Made with ❤️ by the wcauto community
  </p>
  
  <p>
    <a href="https://github.com/YangShengzhou03/wcauto/issues">Report Bug</a> • 
    <a href="https://github.com/YangShengzhou03/wcauto/issues">Request Feature</a> • 
    <a href="https://github.com/YangShengzhou03/wcauto/discussions">Discuss</a>
  </p>
</div>