import win32gui
import win32con

def find_and_close_specific_window(target_class="Chrome_WidgetWin_0", target_title="微信"):
    """查找并关闭特定窗口"""
    found_window = None
    
    def find_window_callback(hwnd, lParam):
        nonlocal found_window
        
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            class_name = win32gui.GetClassName(hwnd)
            
            if class_name == target_class and window_title == target_title:
                found_window = hwnd
                return False
        
        return True
    
    win32gui.EnumWindows(find_window_callback, None)
    
    if found_window:
        print("有符合条件的窗口，需要关闭")
        win32gui.PostMessage(found_window, win32con.WM_CLOSE, 0, 0)
    else:
        print("没有符合条件的窗口，无需关闭")

if __name__ == "__main__":
    find_and_close_specific_window()