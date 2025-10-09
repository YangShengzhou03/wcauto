import time
import pyautogui
import pyperclip
import uiautomation as auto
from ctypes import windll
import psutil

class WeChat:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self._wechat_window_cache = None
    
    def copy_to_clipboard(self, text):
        try:
            pyperclip.copy(text)
            return True
        except Exception:
            return False
    
    def paste_text(self):
        try:
            pyautogui.hotkey('ctrl', 'v')
            return True
        except Exception:
            try:
                pyautogui.keyDown('ctrl')
                pyautogui.press('v')
                pyautogui.keyUp('ctrl')
                return True
            except Exception:
                return False
    
    def find_wechat_window(self):
        if self._wechat_window_cache:
            return self._wechat_window_cache
            
        try:
            all_windows = []
            
            def collect_windows(control, depth=0):
                if depth > 10:
                    return
                if control.ControlTypeName == 'WindowControl':
                    all_windows.append(control)
                for child in control.GetChildren():
                    collect_windows(child, depth + 1)
            
            collect_windows(auto.GetRootControl())
            
            for window in all_windows:
                window_name = window.Name if window.Name else ""
                class_name = window.ClassName if window.ClassName else ""
                
                if ("微信" in window_name or "WeChat" in window_name or 
                    "WeChat" in class_name or "微信" in class_name or
                    "Chat" in class_name):
                    self._wechat_window_cache = window
                    return window
            
            return None
        except Exception:
            return None
    
    def activate_wechat(self):
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                return False
            
            hwnd = wechat_window.NativeWindowHandle
            
            if wechat_window.IsOffscreen:
                windll.user32.ShowWindow(hwnd, 9)
                time.sleep(0.3)
            
            windll.user32.SetForegroundWindow(hwnd)
            time.sleep(0.3)
            
            return True
        except Exception:
            return False
    
    def click_message_input_area(self):
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                return False
            
            rect = wechat_window.BoundingRectangle
            if not rect:
                return False
            
            input_x = rect.right - 200
            input_y = rect.bottom - 80
            
            input_x = max(0, min(input_x, self.screen_width - 1))
            input_y = max(0, min(input_y, self.screen_height - 1))
            
            pyautogui.click(input_x, input_y)
            time.sleep(0.2)
            return True
            
        except Exception:
            return self._click_input_area_fallback()
    
    def _click_input_area_fallback(self):
        try:
            center_x = self.screen_width // 2
            input_y = self.screen_height - 200
            
            center_x = max(0, min(center_x, self.screen_width - 1))
            input_y = max(0, min(input_y, self.screen_height - 1))
            
            pyautogui.click(center_x, input_y)
            time.sleep(0.2)
            return True
        except Exception:
            return False
    
    def click_send_button(self):
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                return False
            
            rect = wechat_window.BoundingRectangle
            if not rect:
                return False
            
            send_x = rect.right - 100
            send_y = rect.bottom - 50
            
            send_x = max(0, min(send_x, self.screen_width - 1))
            send_y = max(0, min(send_y, self.screen_height - 1))
            
            pyautogui.click(send_x, send_y)
            time.sleep(0.2)
            return True
            
        except Exception:
            return False
    
    def SendMsg(self, contact_name, message, use_send_button=False):
        try:
            if not self.activate_wechat():
                return False
            
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1.0)
            
            if not self.copy_to_clipboard(contact_name):
                return False
            time.sleep(0.2)
            
            if not self.paste_text():
                return False
            time.sleep(0.3)
            
            pyautogui.press('enter')
            time.sleep(1.5)
            
            if not self.click_message_input_area():
                pyautogui.press('tab')
                time.sleep(0.3)
            
            if not self.copy_to_clipboard(message):
                return False
            time.sleep(0.2)
            
            if not self.paste_text():
                return False
            time.sleep(0.3)
            
            if use_send_button:
                if not self.click_send_button():
                    pyautogui.press('enter')
            else:
                pyautogui.press('enter')
            
            return True
            
        except Exception:
            return self._send_message_backup(contact_name, message, use_send_button)
    
    def _send_message_backup(self, contact_name, message, use_send_button=False):
        try:
            if not self.activate_wechat():
                return False
            
            pyautogui.keyDown('ctrl')
            pyautogui.press('f')
            pyautogui.keyUp('ctrl')
            time.sleep(1.0)
            
            pyperclip.copy(contact_name)
            time.sleep(0.2)
            
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            time.sleep(0.3)
            
            pyautogui.press('enter')
            time.sleep(1.5)
            
            self.click_message_input_area()
            
            pyperclip.copy(message)
            time.sleep(0.2)
            
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            time.sleep(0.3)
            
            if use_send_button:
                if not self.click_send_button():
                    pyautogui.press('enter')
            else:
                pyautogui.press('enter')
            
            return True
            
        except Exception:
            return False
    
    def check_wechat_running(self):
        try:
            for process in psutil.process_iter(['name']):
                if process.info['name'] and ('WeChat' in process.info['name'] or '微信' in process.info['name']):
                    return True
            return False
        except Exception:
            return False

if __name__ == "__main__":
    wx = WeChat()
    wx.SendMsg("文件传输助手", "测试成功了！")
