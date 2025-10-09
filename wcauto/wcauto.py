import time
import os
import pyautogui
import pyperclip
import uiautomation as auto
from ctypes import windll
import psutil
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WeChat:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self._wechat_window_cache = None
    
    def copy_to_clipboard(self, text):
        """复制文本到剪贴板"""
        try:
            pyperclip.copy(text)
            return True
        except Exception as e:
            logger.error(f"复制到剪贴板失败: {e}")
            return False
    
    def paste_text(self):
        """粘贴剪贴板内容"""
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
        """查找微信窗口"""
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
        """激活微信窗口"""
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                logger.warning("未找到微信窗口")
                return False
            
            hwnd = wechat_window.NativeWindowHandle
            
            if wechat_window.IsOffscreen:
                windll.user32.ShowWindow(hwnd, 9)
                time.sleep(0.3)
            
            windll.user32.SetForegroundWindow(hwnd)
            time.sleep(0.3)
            
            return True
        except Exception as e:
            logger.error(f"激活微信窗口失败: {e}")
            return False
    
    def click_message_input_area(self):
        """点击消息输入区域"""
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
            
        except Exception as e:
            logger.warning(f"点击消息输入区域失败，尝试备用方法: {e}")
            return self._click_input_area_fallback()
    
    def _click_input_area_fallback(self):
        """点击消息输入区域的备用方法"""
        try:
            center_x = self.screen_width // 2
            input_y = self.screen_height - 200
            
            center_x = max(0, min(center_x, self.screen_width - 1))
            input_y = max(0, min(input_y, self.screen_height - 1))
            
            pyautogui.click(center_x, input_y)
            time.sleep(0.2)
            return True
        except Exception as e:
            logger.error(f"备用点击消息输入区域方法失败: {e}")
            return False
    
    def click_send_button(self):
        """点击发送按钮"""
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
            
        except Exception as e:
            logger.error(f"点击发送按钮失败: {e}")
            return False
    
    def SendMsg(self, message, contact_name=None, use_send_button=False):
        """
        发送消息到指定联系人
        
        Args:
            message: 要发送的消息内容
            contact_name: 联系人名称，如果为None则发送到当前聊天
            use_send_button: 是否使用发送按钮发送，默认为False（使用Enter键）
        
        Returns:
            bool: 发送成功返回True，失败返回False
        """
        try:
            if not self.activate_wechat():
                logger.error("无法激活微信窗口")
                return False
            
            # 如果指定了联系人，则搜索联系人
            if contact_name:
                pyautogui.hotkey('ctrl', 'f')
                time.sleep(1.0)
                
                if not self.copy_to_clipboard(contact_name):
                    logger.error("无法复制联系人名称到剪贴板")
                    return False
                time.sleep(0.2)
                
                if not self.paste_text():
                    logger.error("无法粘贴联系人名称")
                    return False
                time.sleep(0.3)
                
                pyautogui.press('enter')
                time.sleep(1.5)
            
            # 点击消息输入区域
            if not self.click_message_input_area():
                pyautogui.press('tab')
                time.sleep(0.3)
            
            # 输入消息
            if not self.copy_to_clipboard(message):
                logger.error("无法复制消息到剪贴板")
                return False
            time.sleep(0.2)
            
            if not self.paste_text():
                logger.error("无法粘贴消息")
                return False
            time.sleep(0.3)
            
            # 发送消息
            if use_send_button:
                if not self.click_send_button():
                    pyautogui.press('enter')
            else:
                pyautogui.press('enter')
            
            logger.info(f"成功发送消息到{'联系人' if contact_name else '当前聊天'}")
            return True
            
        except Exception as e:
            logger.error(f"发送消息失败: {e}")
            return self._send_message_backup(message, contact_name, use_send_button)
    
    def _send_message_backup(self, message, contact_name=None, use_send_button=False):
        """发送消息的备用方法"""
        try:
            if not self.activate_wechat():
                return False
            
            # 如果指定了联系人，则搜索联系人
            if contact_name:
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
            
        except Exception as e:
            logger.error(f"备用发送消息方法失败: {e}")
            return False
    
    def check_wechat_running(self):
        """检查微信是否正在运行"""
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
            
            # 如果指定了联系人，则搜索联系人
            if who:
                pyautogui.hotkey('ctrl', 'f')
                time.sleep(1.0)
                
                if not self.copy_to_clipboard(who):
                    logger.error("无法复制联系人名称到剪贴板")
                    return False
                time.sleep(0.2)
                
                if not self.paste_text():
                    logger.error("无法粘贴联系人名称")
                    return False
                time.sleep(0.3)
                
                pyautogui.press('enter')
                time.sleep(1.5)
            
            # 点击消息输入区域
            if not self.click_message_input_area():
                pyautogui.press('tab')
                time.sleep(0.3)
            
            # 输入消息
            # 确保文件或文件夹存在
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"路径不存在: {filepath}")

            # 转换为绝对路径
            filepath = os.path.abspath(filepath)
            
            # 调用Windows API将文件/文件夹复制到剪贴板
            self._set_clipboard_files([filepath])
            
            if not self.paste_text():
                logger.error("无法粘贴消息")
                return False
            time.sleep(0.3)
            
            # 发送消息
            pyautogui.press('enter')
            
            logger.info(f"成功发送文件到{'联系人' if who else '当前聊天'}")
            return True
        except Exception as e:
            logger.error(f"发送文件失败: {e}")
            return False


    def _set_clipboard_files(self, file_paths):
        """使用Windows API将文件列表设置到剪贴板"""
        import ctypes
        from ctypes import wintypes
        
        # 定义Windows常量和结构
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
        
        # 获取Windows API函数
        kernel32 = ctypes.windll.kernel32
        user32 = ctypes.windll.user32
        
        # 准备文件路径数据
        data = ""
        for path in file_paths:
            # 使用Unicode宽字符格式，每个路径后跟两个空字符
            data += path + "\0"
        data += "\0"  # 最终以两个空字符结束
        
        # 转换为UTF-16 LE编码（Windows宽字符格式）
        data_wide = data.encode('utf-16le')
        
        # 计算总内存大小
        df_size = ctypes.sizeof(DROPFILES)
        total_size = df_size + len(data_wide)
        
        # 分配全局内存
        hGlobal = kernel32.GlobalAlloc(GHND, total_size)
        if not hGlobal:
            raise MemoryError("无法分配全局内存")
        
        try:
            # 锁定内存并获取指针
            pGlobal = kernel32.GlobalLock(hGlobal)
            if not pGlobal:
                raise MemoryError("无法锁定全局内存")
            
            try:
                # 初始化DROPFILES结构
                df = DROPFILES()
                df.pFiles = df_size  # 文件列表在结构体后的偏移量
                df.fWide = True  # 使用Unicode
                
                # 复制结构体到内存
                ctypes.memmove(pGlobal, ctypes.byref(df), df_size)
                
                # 复制文件路径数据到内存
                data_ptr = ctypes.cast(pGlobal + df_size, ctypes.c_void_p)
                ctypes.memmove(data_ptr, data_wide, len(data_wide))
                
            finally:
                kernel32.GlobalUnlock(hGlobal)
            
            # 打开剪贴板并设置数据
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
