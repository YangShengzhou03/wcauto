import win32gui
import win32con

def find_chrome_window_and_close() -> bool:
    def find_window_callback(hwnd, _):
        if (win32gui.IsWindowVisible(hwnd) and 
            win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and 
            win32gui.GetWindowText(hwnd) == "微信"):
            print("有符合条件的窗口，需要关闭")
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            return False
        return True

    return not win32gui.EnumWindows(find_window_callback, None)

if __name__ == "__main__":
    find_chrome_window_and_close()