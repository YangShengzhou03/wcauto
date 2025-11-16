import os
import time
import re
from ctypes import windll, c_void_p, c_char, byref
from typing import Optional, Tuple, List, Callable, TypeVar, Any, Dict

import psutil
import pyautogui
import pyperclip
import uiautomation as auto
import win32con
import win32gui
import win32process
import win32api

from wcauto.wx_response import WxResponse

T = TypeVar('T')


class WeChatMemory:
    def __init__(self) -> None:
        self.screen_width, self.screen_height = pyautogui.size()
        self._wechat_window_cache: Optional[auto.WindowControl] = None
        self._wechat_process = None
        self._process_handle = None
        if not self.activate_wechat():
            raise RuntimeError("微信未启动")
        # 初始化微信进程信息
        self._find_wechat_process()

    def _handle_operation(self, operation_name: str, operation: Callable[[], T], 
                         error_message: str = "操作失败") -> T:
        try:
            return operation()
        except Exception as e:
            raise RuntimeError(f"{error_message}: {e}") from e

    def _safe_window_operation(self, operation: str, *args: Any, **kwargs: Any) -> bool:
        return self._handle_operation(
            "window_operation",
            lambda: self._execute_window_operation(operation, *args, **kwargs),
            "窗口操作失败"
        )

    def _execute_window_operation(self, operation: str, *args: Any, **kwargs: Any) -> bool:
        wechat_window = self.find_wechat_window()
        if not wechat_window:
            return False
        
        if operation == "click":
            x, y = args
            safe_x, safe_y = self._get_safe_coordinates(x, y)
            pyautogui.click(safe_x, safe_y)
            time.sleep(0.1)
            return True
        elif operation == "activate":
            return self._activate_window(wechat_window)
        
        return False

    def _activate_window(self, window: auto.WindowControl) -> bool:
        hwnd = window.NativeWindowHandle
        
        is_minimized = windll.user32.IsIconic(hwnd)
        is_visible = windll.user32.IsWindowVisible(hwnd)
        is_on_desktop = not window.IsOffscreen
        is_foreground = (hwnd == windll.user32.GetForegroundWindow())
        
        if not is_visible or is_minimized or not is_on_desktop or not is_foreground:
            pyautogui.hotkey('ctrl', 'alt', 'w')
            time.sleep(1)
            
            if is_minimized or not is_on_desktop:
                windll.user32.ShowWindow(hwnd, 9)
                time.sleep(1)
        
        if not windll.user32.SetForegroundWindow(hwnd):
            pyautogui.hotkey('ctrl', 'alt', 'w')
            time.sleep(1)
            if not windll.user32.SetForegroundWindow(hwnd):
                raise RuntimeError("无法将微信窗口设置到前台")
        
        time.sleep(0.5)
        return True

    def copy_to_clipboard(self, text: str) -> bool:
        return self._handle_operation(
            "copy_to_clipboard",
            lambda: self._execute_copy_to_clipboard(text),
            "复制到剪贴板失败"
        )

    def _execute_copy_to_clipboard(self, text: str) -> bool:
        pyperclip.copy(text)
        return True

    def paste_text(self) -> bool:
        return self._handle_operation(
            "paste_text",
            lambda: self._execute_paste_text(),
            "粘贴文本失败"
        )

    def _execute_paste_text(self) -> bool:
        pyautogui.hotkey('ctrl', 'v')
        return True

    def find_wechat_window(self) -> Optional[auto.WindowControl]:
        if self._wechat_window_cache:
            return self._wechat_window_cache

        return self._handle_operation(
            "find_wechat_window",
            lambda: self._execute_find_wechat_window(),
            "查找微信窗口失败"
        )

    def _execute_find_wechat_window(self) -> Optional[auto.WindowControl]:
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

    def activate_wechat(self) -> bool:
        return self._handle_operation(
            "activate_wechat",
            lambda: self._execute_activate_wechat(),
            "激活微信窗口失败"
        )

    def _execute_activate_wechat(self) -> bool:
        wechat_window = self.find_wechat_window()
        if not wechat_window:
            pyautogui.hotkey('ctrl', 'alt', 'w')
            time.sleep(1)

            wechat_window = self.find_wechat_window()
            if not wechat_window:
                raise RuntimeError("即使检查进程，仍未找到微信窗口")

        return self._activate_window(wechat_window)

    def find_chrome_window_and_close(self) -> bool:
        return self._handle_operation(
            "find_chrome_window_and_close",
            lambda: self._execute_find_chrome_window_and_close(),
            "查找并关闭Chrome窗口失败"
        )

    def _execute_find_chrome_window_and_close(self) -> bool:
        flags = False
        def find_window_callback(hwnd, _):
            nonlocal flags
            if (win32gui.IsWindowVisible(hwnd) and
                    win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and
                    win32gui.GetWindowText(hwnd) == "微信"):
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                flags = True
                return False
            return True
        win32gui.EnumWindows(find_window_callback, None)
        return flags

    def _get_safe_coordinates(self, x: int, y: int) -> Tuple[int, int]:
        return max(0, min(x, self.screen_width - 1)), max(0, min(y, self.screen_height - 1))

    def click_message_input_area(self) -> bool:
        return self._handle_operation(
            "click_message_input_area",
            lambda: self._execute_click_message_input_area(),
            "点击消息输入区域失败"
        )

    def _execute_click_message_input_area(self) -> bool:
        wechat_window = self.find_wechat_window()
        if not wechat_window:
            return False

        rect = wechat_window.BoundingRectangle
        if not rect:
            return False

        input_x, input_y = self._get_safe_coordinates(rect.right - 300, rect.bottom - 80)
        return self._safe_window_operation("click", input_x, input_y)

    def click_send_button(self) -> bool:
        return self._handle_operation(
            "click_send_button",
            lambda: self._execute_click_send_button(),
            "点击发送按钮失败"
        )

    def _execute_click_send_button(self) -> bool:
        wechat_window = self.find_wechat_window()
        if not wechat_window:
            return False

        rect = wechat_window.BoundingRectangle
        if not rect:
            return False

        send_x, send_y = self._get_safe_coordinates(rect.right - 100, rect.bottom - 50)
        return self._safe_window_operation("click", send_x, send_y)

    def _search_contact(self, contact_name: str) -> bool:
        return self._handle_operation(
            "search_contact",
            lambda: self._execute_search_contact(contact_name),
            "搜索联系人失败"
        )

    def _execute_search_contact(self, contact_name: str) -> bool:
        wechat_window = self.find_wechat_window()
        if not wechat_window:
            raise RuntimeError("微信窗口未找到")
        
        if not self._activate_window(wechat_window):
            raise RuntimeError("无法激活微信窗口进行搜索")
        
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.5)

        if not self.copy_to_clipboard(contact_name):
            raise RuntimeError("无法复制联系人名称到剪贴板")
        time.sleep(0.1)

        if not self.paste_text():
            raise RuntimeError("无法粘贴联系人名称")
        time.sleep(0.5)

        pyautogui.press('enter')
        time.sleep(1.0)

        if self.find_chrome_window_and_close():
            raise RuntimeError(f"未找到备注为 {contact_name} 的联系人")
        return True

    def _prepare_message_area(self) -> bool:
        return self.click_message_input_area()

    def _send_content(self, content: Any, content_type: str = "text", 
                      use_send_button: bool = False) -> bool:
        if content_type == "text":
            return self._send_text_content(content, use_send_button)
        elif content_type == "file":
            return self._send_file_content(content)
        else:
            raise ValueError(f"不支持的内容类型: {content_type}")

    def _send_text_content(self, message: str, use_send_button: bool = False) -> bool:
        return self._handle_operation(
            "send_text_content",
            lambda: self._execute_send_text_content(message, use_send_button),
            "发送文本内容失败"
        )

    def _execute_send_text_content(self, message: str, use_send_button: bool = False) -> bool:
        if not self.copy_to_clipboard(message):
            raise RuntimeError("无法复制消息到剪贴板")
        time.sleep(0.1)

        if not self.paste_text():
            raise RuntimeError("无法粘贴消息")
        time.sleep(0.1)

        if use_send_button:
            if not self.click_send_button():
                pyautogui.press('enter')
        else:
            pyautogui.press('enter')
        return True

    def _send_file_content(self, filepath: str) -> bool:
        return self._handle_operation(
            "send_file_content",
            lambda: self._execute_send_file_content(filepath),
            "发送文件内容失败"
        )

    def _execute_send_file_content(self, filepath: str) -> bool:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"路径不存在: {filepath}")

        filepath = os.path.abspath(filepath)
        self._set_clipboard_files([filepath])

        if not self.paste_text():
            raise RuntimeError("无法粘贴文件")
        time.sleep(0.1)

        pyautogui.press('enter')
        return True

    def _prepare_send_operation(self, who: Optional[str] = None) -> WxResponse:
        if not self.activate_wechat():
            return WxResponse.failure(
                message="无法激活微信窗口",
                data={"operation": "activate_wechat", "target": who or "当前聊天"}
            )
        
        if who and not self._search_contact(who):
            return WxResponse.failure(
                message="搜索联系人失败",
                data={"operation": "search_contact", "contact_name": who}
            )

        if not self._prepare_message_area():
            return WxResponse.failure(
                message="没找到信息发送区域",
                data={"operation": "prepare_message_area", "target": who or "当前聊天"}
            )
        
        return WxResponse.success("准备完成", {"target": who or "当前聊天"})

    def send_msg(self, msg: str, who: Optional[str] = None, use_send_button: bool = False) -> WxResponse:
        try:
            prep_result = self._prepare_send_operation(who)
            if not prep_result.success:
                return prep_result

            if not self._send_content(msg, "text", use_send_button):
                return WxResponse.failure(
                    message="发送消息内容失败",
                    data={"operation": "send_message_content", "message_length": len(msg), "use_send_button": use_send_button}
                )

            return WxResponse.success(
                message=f"成功发送消息到{'联系人' if who else '当前聊天'}",
                data={
                    "operation": "send_message",
                    "target": who or "当前聊天",
                    "message_length": len(msg),
                    "use_send_button": use_send_button,
                    "timestamp": time.time()
                }
            )

        except Exception as e:
            return WxResponse.error(
                message=f"发送消息失败: {e}",
                data={
                    "operation": "send_message",
                    "target": who or "当前聊天",
                    "error_type": type(e).__name__,
                    "timestamp": time.time()
                }
            )

    def check_wechat_running(self) -> bool:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] and ('WeChat' in proc.info['name'] or '微信' in proc.info['name']):
                return True
        return False
    
    def _find_wechat_process(self) -> Optional[psutil.Process]:
        """查找微信进程"""
        try:
            for proc in psutil.process_iter(['name', 'pid']):
                if proc.info['name'] and ('WeChat.exe' == proc.info['name'] or '微信.exe' == proc.info['name']):
                    self._wechat_process = proc
                    return proc
            return None
        except Exception as e:
            print(f"查找微信进程失败: {e}")
            return None
    
    def _open_process_handle(self, pid: int) -> Optional[int]:
        """打开进程句柄"""
        try:
            # PROCESS_VM_READ = 0x0010
            # PROCESS_QUERY_INFORMATION = 0x0400
            PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
            handle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
            self._process_handle = handle
            return handle
        except Exception as e:
            print(f"打开进程句柄失败: {e}")
            return None
    
    def _close_process_handle(self) -> None:
        """关闭进程句柄"""
        if self._process_handle:
            try:
                win32api.CloseHandle(self._process_handle)
                self._process_handle = None
            except Exception as e:
                print(f"关闭进程句柄失败: {e}")
    
    def read_memory_string(self, address: int, size: int = 512) -> Optional[str]:
        """从指定内存地址读取字符串"""
        if not self._process_handle:
            if not self._wechat_process:
                self._find_wechat_process()
            if self._wechat_process:
                self._open_process_handle(self._wechat_process.pid)
            else:
                return None
        
        try:
            buffer = (c_char * size)()
            bytes_read = c_void_p()
            result = windll.kernel32.ReadProcessMemory(
                self._process_handle,
                c_void_p(address),
                byref(buffer),
                size,
                byref(bytes_read)
            )
            
            if result:
                # 尝试解码为UTF-8和GBK
                try:
                    return buffer.value.decode('utf-8').strip('\x00')
                except UnicodeDecodeError:
                    try:
                        return buffer.value.decode('gbk').strip('\x00')
                    except UnicodeDecodeError:
                        return None
            return None
        except Exception as e:
            print(f"读取内存失败: {e}")
            return None
    
    def scan_for_strings(self, pattern: Optional[str] = None, min_length: int = 5, max_size: int = 1024*1024*10) -> List[str]:
        """扫描微信进程内存中的字符串
        
        Args:
            pattern: 可选的正则表达式模式，用于过滤字符串
            min_length: 最小字符串长度
            max_size: 最大扫描内存大小
            
        Returns:
            找到的字符串列表
        """
        if not self._wechat_process:
            self._find_wechat_process()
            if not self._wechat_process:
                return []
        
        handle = self._open_process_handle(self._wechat_process.pid)
        if not handle:
            return []
        
        found_strings = set()
        regex = re.compile(pattern) if pattern else None
        
        try:
            # 获取进程的内存映射
            modules = win32process.EnumProcessModules(handle)
            
            for module in modules:
                try:
                    module_info = win32process.GetModuleInformation(
                        handle, module, win32process.ModuleInfo()
                    )
                    base_address = module_info.lpBaseOfDll
                    module_size = module_info.SizeOfImage
                    
                    # 限制扫描大小
                    if module_size > max_size:
                        continue
                    
                    # 读取内存块
                    buffer = win32process.ReadProcessMemory(handle, base_address, module_size)
                    
                    # 寻找连续的可打印字符
                    current_str = []
                    for byte in buffer:
                        # 可打印字符范围（包括中文）
                        if 32 <= byte <= 126 or byte in [9, 10, 13] or (128 <= byte <= 255):
                            current_str.append(chr(byte))
                        else:
                            if len(current_str) >= min_length:
                                text = ''.join(current_str)
                                # 过滤掉大部分是空格或不可打印字符的字符串
                                if len(text.strip()) >= min_length // 2:
                                    # 如果指定了模式，进行匹配
                                    if not regex or regex.search(text):
                                        # 尝试解码可能的多字节字符
                                        try:
                                            # 检查是否包含中文（简单判断）
                                            has_chinese = any(ord(c) > 127 for c in text)
                                            if has_chinese:
                                                # 尝试不同的编码
                                                for encoding in ['utf-8', 'gbk', 'gb2312']:
                                                    try:
                                                        # 这里简化处理，实际需要更复杂的逻辑
                                                        found_strings.add(text)
                                                        break
                                                    except:
                                                        continue
                                            else:
                                                found_strings.add(text)
                                        except:
                                            pass
                            current_str = []
                    
                except Exception as e:
                    # 跳过无法读取的模块
                    continue
                    
        except Exception as e:
            print(f"扫描内存失败: {e}")
        finally:
            self._close_process_handle()
        
        return list(found_strings)
    
    def get_visible_chat_messages(self) -> List[str]:
        """获取当前在屏幕上可见的聊天消息
        
        Returns:
            聊天消息列表
        """
        # 由于无法确定具体的消息内存地址模式，这里采用更通用的方法
        # 扫描内存中可能的聊天消息模式
        patterns = [
            r'[\u4e00-\u9fa5]{2,}',  # 至少2个中文字符
            r'^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+$',  # 邮箱
            r'^https?://[\w\-]+(\.[\w\-]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?$',  # URL
        ]
        
        all_messages = []
        
        # 尝试不同的模式扫描
        for pattern in patterns:
            messages = self.scan_for_strings(pattern=pattern, min_length=5)
            all_messages.extend(messages)
        
        # 也进行通用扫描，捕获其他可能的消息
        general_messages = self.scan_for_strings(min_length=10)
        all_messages.extend(general_messages)
        
        # 去重并按长度排序（长消息更可能是有意义的）
        unique_messages = list(set(all_messages))
        unique_messages.sort(key=len, reverse=True)
        
        # 返回前100条最有可能的消息
        return unique_messages[:100]

    def _set_clipboard_files(self, filepaths: List[str]) -> None:
        import win32clipboard
        import win32con
        
        file_list = '\0'.join(filepaths) + '\0'
        file_list = file_list.encode('gbk')
        
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_HDROP, file_list)
        win32clipboard.CloseClipboard()

    def send_files(self, filepath: str, who: Optional[str] = None) -> WxResponse:
        try:
            prep_result = self._prepare_send_operation(who)
            if not prep_result.success:
                return prep_result

            if not self._send_content(filepath, "file"):
                return WxResponse.failure(
                    message="发送文件内容失败",
                    data={"operation": "send_file_content", "filepath": filepath}
                )

            return WxResponse.success(
                message=f"成功发送文件到{'联系人' if who else '当前聊天'}",
                data={
                    "operation": "send_file",
                    "target": who or "当前聊天",
                    "filepath": filepath,
                    "filename": os.path.basename(filepath),
                    "file_size": os.path.getsize(filepath),
                    "timestamp": time.time()
                }
            )

        except Exception as e:
            return WxResponse.error(
                message=f"发送文件失败: {e}",
                data={
                    "operation": "send_file",
                    "target": who or "当前聊天",
                    "error_type": type(e).__name__,
                    "timestamp": time.time()
                }
            )

    def send_multiple_files(self, filepaths: List[str], who: Optional[str] = None) -> WxResponse:
        try:
            if not filepaths:
                return WxResponse.failure("文件列表为空", {"operation": "send_multiple_files"})
            
            for filepath in filepaths:
                if not os.path.exists(filepath):
                    return WxResponse.failure(
                        f"文件不存在: {filepath}",
                        {"operation": "send_multiple_files", "filepath": filepath}
                    )

            prep_result = self._prepare_send_operation(who)
            if not prep_result.success:
                return prep_result

            self._set_clipboard_files(filepaths)
            
            if not self.paste_text():
                return WxResponse.failure(
                    "无法粘贴文件",
                    {"operation": "send_multiple_files", "file_count": len(filepaths)}
                )
            time.sleep(0.1)

            pyautogui.press('enter')
            
            return WxResponse.success(
                f"成功发送{len(filepaths)}个文件到{'联系人' if who else '当前聊天'}",
                {
                    "operation": "send_multiple_files",
                    "target": who or "当前聊天",
                    "file_count": len(filepaths),
                    "filepaths": filepaths,
                    "timestamp": time.time()
                }
            )

        except Exception as e:
            return WxResponse.error(
                f"发送多个文件失败: {e}",
                {
                    "operation": "send_multiple_files",
                    "target": who or "当前聊天",
                    "error_type": type(e).__name__,
                    "timestamp": time.time()
                }
            )


if __name__ == "__main__":
    wx = WeChat()
    result = wx.send_msg("Hello", "文件传输助手")
    print(result)