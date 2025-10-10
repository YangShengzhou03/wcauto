import ctypes
from ctypes import wintypes
import win32gui
import win32con
import win32process
import win32api

def enum_windows_proc(hwnd, lParam):
    """窗口枚举回调函数"""
    if win32gui.IsWindowVisible(hwnd):
        # 获取窗口标题
        window_title = win32gui.GetWindowText(hwnd)
        
        # 获取窗口类名
        class_name = win32gui.GetClassName(hwnd)
        
        # 获取进程ID
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        
        # 获取窗口样式
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        
        # 过滤掉没有标题的窗口和一些系统窗口
        if window_title and (style & win32con.WS_OVERLAPPEDWINDOW) and not (style & win32con.WS_CHILD):
            print(f"句柄: {hwnd}")
            print(f"窗口类: {class_name}")
            print(f"窗口标题: {window_title}")
            print(f"进程ID: {pid}")
            print("-" * 50)
    
    return True

def get_all_windows():
    """获取所有可见窗口"""
    print("正在枚举桌面上的所有可见窗口...")
    print("=" * 60)
    
    # 枚举所有顶层窗口
    win32gui.EnumWindows(enum_windows_proc, None)

def get_windows_with_uia():
    """使用UI Automation获取窗口信息"""
    try:
        import comtypes.client
        
        # 确保UIAutomation类型库已注册
        try:
            from comtypes.gen import UIAutomationClient
        except ImportError:
            # 如果类型库未注册，尝试注册
            comtypes.client.GetModule(("{944DE083-8FB8-45CF-BCB7-C477ACB2F897}", 1, 0))
            from comtypes.gen import UIAutomationClient
        
        # 创建UIAutomation实例
        uia = comtypes.client.CreateObject("{FF48DBA4-60EF-4201-AA87-54103EEF594E}", interface=UIAutomationClient.IUIAutomation)
        
        # 获取桌面元素
        desktop = uia.GetRootElement()
        
        # 创建条件：查找所有窗口
        condition = uia.CreateTrueCondition()
        
        # 获取所有顶层元素
        elements = desktop.FindAll(UIAutomationClient.TreeScope_Children, condition)
        
        print("使用UI Automation获取的窗口信息:")
        print("=" * 60)
        
        window_count = 0
        for i in range(elements.Length):
            try:
                element = elements.GetElement(i)
                
                # 检查是否是窗口（有窗口模式）
                window_pattern = element.GetCurrentPattern(UIAutomationClient.UIA_WindowPatternId)
                if window_pattern:
                    # 获取窗口句柄
                    hwnd = element.CurrentNativeWindowHandle
                    
                    # 获取窗口标题
                    name = element.CurrentName
                    
                    # 获取窗口类名
                    class_name = element.CurrentClassName if hasattr(element, 'CurrentClassName') else "N/A"
                    
                    # 获取自动化ID
                    automation_id = element.CurrentAutomationId
                    
                    if name and hwnd:  # 只显示有标题和句柄的窗口
                        window_count += 1
                        print(f"窗口 {window_count}:")
                        print(f"  句柄: {hwnd}")
                        print(f"  窗口类: {class_name}")
                        print(f"  窗口标题: {name}")
                        print(f"  自动化ID: {automation_id}")
                        print("-" * 50)
                        
            except Exception as e:
                continue
        
        if window_count == 0:
            print("未找到任何窗口，尝试使用备选方法...")
            return False
                
    except ImportError:
        print("未安装comtypes库，无法使用UI Automation")
        print("请运行: pip install comtypes")
        return False
    except Exception as e:
        print(f"UI Automation错误: {e}")
        return False
    
    return True

def find_and_close_specific_window(target_class="Chrome_WidgetWin_0", target_title="微信"):
    """查找并关闭特定窗口"""
    print(f"正在查找窗口类为 '{target_class}' 且标题为 '{target_title}' 的窗口...")
    print("=" * 60)
    
    found_window = None
    
    def find_window_callback(hwnd, lParam):
        nonlocal found_window
        
        if win32gui.IsWindowVisible(hwnd):
            # 获取窗口标题和类名
            window_title = win32gui.GetWindowText(hwnd)
            class_name = win32gui.GetClassName(hwnd)
            
            # 检查是否匹配目标窗口
            if class_name == target_class and window_title == target_title:
                found_window = hwnd
                return False  # 停止枚举
        
        return True  # 继续枚举
    
    # 枚举所有窗口查找目标窗口
    win32gui.EnumWindows(find_window_callback, None)
    
    if found_window:
        print(f"找到目标窗口!")
        print(f"句柄: {found_window}")
        print(f"窗口类: {target_class}")
        print(f"窗口标题: {target_title}")
        
        # 尝试关闭窗口
        try:
            # 发送关闭消息
            win32gui.PostMessage(found_window, win32con.WM_CLOSE, 0, 0)
            print("已发送关闭消息到目标窗口")
            return True
        except Exception as e:
            print(f"关闭窗口时出错: {e}")
            return True
    else:
        print("没有符合条件的窗口，无需关闭")
        return False

if __name__ == "__main__":
    print("桌面窗口信息获取工具")
    print("=" * 60)
    
    # 首先执行查找并关闭特定窗口的功能
    find_and_close_specific_window()
    
    print("\n" + "=" * 60)
    print("窗口信息枚举:")
    
    # 然后尝试使用UI Automation获取窗口信息
    if not get_windows_with_uia():
        print("\n使用传统Win32 API获取窗口信息:")
        get_all_windows()
    
    print("\n程序执行完成!")