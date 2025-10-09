import time
import os
import pyautogui
import pyperclip
import uiautomation as auto
from ctypes import windll
import psutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WeChat:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self._wechat_window_cache = None
    
    def copy_to_clipboard(self, text):
        try:
            pyperclip.copy(text)
            return True
        except Exception as e:
            logger.error(f"复制到剪贴板失败: {e}")
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
            except Exception as e:
                logger.error(f"粘贴文本失败: {e}")
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
        except Exception as e:
            logger.error(f"查找微信窗口失败: {e}")
            return None
    
    def activate_wechat(self):
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                logger.warning("未找到微信窗口")
                return False
            
            hwnd = wechat_window.NativeWindowHandle
            
            if wechat_window.IsOffscreen:
                windll.user32.ShowWindow(hwnd, 9)
                time.sleep(0.1)
            
            windll.user32.SetForegroundWindow(hwnd)
            time.sleep(0.1)
            
            return True
        except Exception as e:
            logger.error(f"激活微信窗口失败: {e}")
            return False
    
    def _get_safe_coordinates(self, x, y):
        return max(0, min(x, self.screen_width - 1)), max(0, min(y, self.screen_height - 1))
    
    def click_message_input_area(self):
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                return False
            
            rect = wechat_window.BoundingRectangle
            if not rect:
                return False
            
            input_x, input_y = self._get_safe_coordinates(rect.right - 200, rect.bottom - 80)
            
            pyautogui.click(input_x, input_y)
            time.sleep(0.05)
            return True
            
        except Exception as e:
            logger.warning(f"点击消息输入区域失败，尝试备用方法: {e}")
            return self._click_input_area_fallback()
    
    def _click_input_area_fallback(self):
        try:
            center_x, input_y = self._get_safe_coordinates(self.screen_width // 2, self.screen_height - 200)
            
            pyautogui.click(center_x, input_y)
            time.sleep(0.05)
            return True
        except Exception as e:
            logger.error(f"备用点击消息输入区域方法失败: {e}")
            return False
    
    def click_send_button(self):
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                return False
            
            rect = wechat_window.BoundingRectangle
            if not rect:
                return False
            
            send_x, send_y = self._get_safe_coordinates(rect.right - 100, rect.bottom - 50)
            
            pyautogui.click(send_x, send_y)
            time.sleep(0.05)
            return True
            
        except Exception as e:
            logger.error(f"点击发送按钮失败: {e}")
            return False
    
    def _search_contact(self, contact_name):
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.2)
        
        if not self.copy_to_clipboard(contact_name):
            logger.error("无法复制联系人名称到剪贴板")
            return False
        time.sleep(0.05)
        
        if not self.paste_text():
            logger.error("无法粘贴联系人名称")
            return False
        time.sleep(0.1)
        
        pyautogui.press('enter')
        time.sleep(0.2)
        return True
    
    def _prepare_message_area(self):
        if not self.click_message_input_area():
            pyautogui.press('tab')
            time.sleep(0.1)
        return True
    
    def _send_message_content(self, message, use_send_button=False):
        if not self.copy_to_clipboard(message):
            logger.error("无法复制消息到剪贴板")
            return False
        time.sleep(0.05)
        
        if not self.paste_text():
            logger.error("无法粘贴消息")
            return False
        time.sleep(0.1)
        
        if use_send_button:
            if not self.click_send_button():
                pyautogui.press('enter')
        else:
            pyautogui.press('enter')
        return True
    
    def SendMsg(self, message, who=None, use_send_button=False):
        try:
            if not self.activate_wechat():
                logger.error("无法激活微信窗口")
                return False
            
            if who and not self._search_contact(who):
                return False
            
            if not self._prepare_message_area():
                return False
            
            if not self._send_message_content(message, use_send_button):
                return False
            
            logger.info(f"成功发送消息到{'联系人' if who else '当前聊天'}")
            return True
            
        except Exception as e:
            logger.error(f"发送消息失败: {e}")
            return self._send_message_backup(message, who, use_send_button)
    
    def _send_message_backup(self, message, who=None, use_send_button=False):
        try:
            if not self.activate_wechat():
                return False
            
            if who:
                pyautogui.keyDown('ctrl')
                pyautogui.press('f')
                pyautogui.keyUp('ctrl')
                time.sleep(0.2)
                
                pyperclip.copy(who)
                time.sleep(0.05)
                
                pyautogui.keyDown('ctrl')
                pyautogui.press('v')
                pyautogui.keyUp('ctrl')
                time.sleep(0.1)
                
                pyautogui.press('enter')
                time.sleep(0.2)
            
            self.click_message_input_area()
            
            pyperclip.copy(message)
            time.sleep(0.05)
            
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            time.sleep(0.1)
            
            if use_send_button:
                if not self.click_send_button():
                    pyautogui.press('enter')
            else:
                pyautogui.press('enter')
            
            return True
            
        except Exception as e:
            logger.error(f"备用发送消息方法失败: {e}")
            return False
    
    def check_wechat_running(self):
        try:
            for process in psutil.process_iter(['name']):
                if process.info['name'] and ('WeChat' in process.info['name'] or '微信' in process.info['name']):
                    return True
            return False
        except Exception as e:
            logger.error(f"检查微信运行状态失败: {e}")
            return False

    def SendFiles(self, filepath, who=None):
        try:
            if not self.activate_wechat():
                logger.error("无法激活微信窗口")
                return False
            
            if who and not self._search_contact(who):
                return False
            
            if not self._prepare_message_area():
                return False
            
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"路径不存在: {filepath}")

            filepath = os.path.abspath(filepath)
            
            self._set_clipboard_files([filepath])
            
            if not self.paste_text():
                logger.error("无法粘贴消息")
                return False
            time.sleep(0.1)
            
            pyautogui.press('enter')
            
            logger.info(f"成功发送文件到{'联系人' if who else '当前聊天'}")
            return True
        except Exception as e:
            logger.error(f"发送文件失败: {e}")
            return False

    def _set_clipboard_files(self, file_paths):
        import ctypes
        from ctypes import wintypes
        
        CF_HDROP = 15
        GMEM_MOVEABLE = 0x0002
        GMEM_ZEROINIT = 0x0040
        GHND = GMEM_MOVEABLE | GMEM_ZEROINIT
        
        class DROPFILES(ctypes.Structure):
            _fields_ = [
                ("pFiles", wintypes.DWORD),
                ("pt", wintypes.POINT),
                ("fNC", wintypes.BOOL),
                ("fWide", wintypes.BOOL)
            ]
        
        kernel32 = ctypes.windll.kernel32
        user32 = ctypes.windll.user32
        
        data = ""
        for path in file_paths:
            data += path + "\0"
        data += "\0"
        
        data_wide = data.encode('utf-16le')
        
        df_size = ctypes.sizeof(DROPFILES)
        total_size = df_size + len(data_wide)
        
        hGlobal = kernel32.GlobalAlloc(GHND, total_size)
        if not hGlobal:
            raise MemoryError("无法分配全局内存")
        
        try:
            pGlobal = kernel32.GlobalLock(hGlobal)
            if not pGlobal:
                raise MemoryError("无法锁定全局内存")
            
            try:
                df = DROPFILES()
                df.pFiles = df_size
                df.fWide = True
                
                ctypes.memmove(pGlobal, ctypes.byref(df), df_size)
                
                data_ptr = ctypes.cast(pGlobal + df_size, ctypes.c_void_p)
                ctypes.memmove(data_ptr, data_wide, len(data_wide))
                
            finally:
                kernel32.GlobalUnlock(hGlobal)
            
            if user32.OpenClipboard(0):
                user32.EmptyClipboard()
                result = user32.SetClipboardData(CF_HDROP, hGlobal)
                user32.CloseClipboard()
                
                if not result:
                    raise RuntimeError("无法设置剪贴板数据")
            else:
                raise RuntimeError("无法打开剪贴板")
                
        except Exception:
            kernel32.GlobalFree(hGlobal)
            raise


if __name__ == "__main__":
    wx = WeChat()
    wx.SendMsg("测试成功了！", "文件传输助手")
