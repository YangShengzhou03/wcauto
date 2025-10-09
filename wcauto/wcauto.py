import time
import os
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

    def SendFiles(self, filepath, who=None):
        """
        发送文件到指定联系人
        
        Args:
            filepath: 文件路径，可以是字符串或列表/元组/集合
            who: 联系人名称
            exact: 是否精确匹配联系人名称（暂未实现）
        
        Returns:
            bool: 发送成功返回True，失败返回False
        """
        filelist = []
        
        # 处理文件路径参数
        if isinstance(filepath, str):
            if not os.path.exists(filepath):
                print(f'未找到文件：{filepath}，无法成功发送')
                return False
            else:
                filelist.append(os.path.realpath(filepath))
        elif isinstance(filepath, (list, tuple, set)):
            for i in filepath:
                if os.path.exists(i):
                    filelist.append(i)
                else:
                    print(f'未找到文件：{i}')
        else:
            print(f'filepath参数格式错误：{type(filepath)}，应为str、list、tuple、set格式')
            return False
        
        if not filelist:
            print('未找到任何有效文件')
            return False
        
        # 激活微信窗口
        if not self.activate_wechat():
            print('无法激活微信窗口')
            return False
        
        # 搜索联系人
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1.0)
        
        if who:
            if not self.copy_to_clipboard(who):
                print('无法复制联系人名称到剪贴板')
                return False
            time.sleep(0.2)
            
            if not self.paste_text():
                print('无法粘贴联系人名称')
                return False
            time.sleep(0.3)
            
            pyautogui.press('enter')
            time.sleep(1.5)
        
        # 点击消息输入区域
        if not self.click_message_input_area():
            pyautogui.press('tab')
            time.sleep(0.3)
        
        # 发送每个文件
        success_count = 0
        for file_path in filelist:
            try:
                # 使用Windows API复制文件到剪贴板
                import win32clipboard
                import win32con
                
                # 打开剪贴板
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                
                # 设置文件路径到剪贴板
                file_paths = [file_path]
                
                # 构建文件列表格式
                file_list = "\0".join(file_paths) + "\0\0"
                
                # 设置CF_HDROP格式（文件拖放格式）
                win32clipboard.SetClipboardData(win32con.CF_HDROP, file_list.encode('utf-16le'))
                
                # 关闭剪贴板
                win32clipboard.CloseClipboard()
                
                time.sleep(0.5)
                
                # 粘贴文件
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1.0)
                
                # 发送文件
                pyautogui.press('enter')
                time.sleep(1.0)
                
                success_count += 1
                print(f'成功发送文件：{os.path.basename(file_path)}')
                
            except Exception as e:
                print(f'发送文件失败：{file_path}, 错误：{e}')
                # 尝试备用方法：使用文件路径作为文本发送
                try:
                    print(f'尝试备用方法发送文件：{file_path}')
                    if self.SendMsg(who, file_path):
                        success_count += 1
                        print(f'备用方法成功发送文件：{os.path.basename(file_path)}')
                except Exception as e2:
                    print(f'备用方法也失败：{e2}')
        
        print(f'成功发送 {success_count}/{len(filelist)} 个文件')
        return success_count > 0

if __name__ == "__main__":
    wx = WeChat()
    wx.SendMsg("文件传输助手", "测试成功了！")
