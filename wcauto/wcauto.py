import os
import time
from ctypes import windll

import psutil
import pyautogui
import pyperclip
import uiautomation as auto
import win32con
import win32gui

from wcauto.WxResponse import WxResponse


class WeChat4:
    def __init__(self) -> None:
        self.screen_width, self.screen_height = pyautogui.size()
        self._wechat_window_cache = None
        if not self.activate_wechat():
            raise RuntimeError("微信未启动")

    def copy_to_clipboard(self, text: str) -> bool:
        try:
            pyperclip.copy(text)
            return True
        except Exception as e:
            raise RuntimeError(f"复制到剪贴板失败: {e}")

    def paste_text(self) -> bool:
        try:
            pyautogui.hotkey('ctrl', 'v')
            return True
        except Exception as e:
            raise RuntimeError(f"粘贴文本失败: {e}")

    def find_wechat_window(self) -> auto.WindowControl | None:
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
            raise RuntimeError(f"查找微信窗口失败: {e}")

    def activate_wechat(self) -> bool:
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                pyautogui.hotkey('ctrl', 'alt', 'w')
                time.sleep(1)

                wechat_window = self.find_wechat_window()
                if not wechat_window:
                    raise RuntimeError("即使检查进程，仍未找到微信窗口")

            hwnd = wechat_window.NativeWindowHandle

            # 检查窗口是否最小化
            is_minimized = windll.user32.IsIconic(hwnd)
            
            # 如果窗口在屏幕外或最小化，需要恢复窗口
            if wechat_window.IsOffscreen or is_minimized:
                # SW_RESTORE = 9，恢复窗口到正常状态
                windll.user32.ShowWindow(hwnd, 9)
                time.sleep(1)

            activation_result = windll.user32.SetForegroundWindow(hwnd)
            if not activation_result:
                pyautogui.hotkey('ctrl', 'alt', 'w')
                time.sleep(1)

                activation_result = windll.user32.SetForegroundWindow(hwnd)
                if not activation_result:
                    raise RuntimeError("即使检查进程，仍未找到微信窗口")

            time.sleep(0.5)
            return True
        except Exception as e:
            raise RuntimeError(f"激活微信窗口失败: {e}")

    def find_chrome_window_and_close(self) -> bool:
        Flags = False
        def find_window_callback(hwnd, _):
            nonlocal Flags
            if (win32gui.IsWindowVisible(hwnd) and
                    win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and
                    win32gui.GetWindowText(hwnd) == "微信"):
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                Flags = True
                return False
            return True
        win32gui.EnumWindows(find_window_callback, None)
        return Flags

    def _get_safe_coordinates(self, x: int, y: int) -> tuple[int, int]:
        return max(0, min(x, self.screen_width - 1)), max(0, min(y, self.screen_height - 1))

    def click_message_input_area(self) -> bool:
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                return False

            rect = wechat_window.BoundingRectangle
            if not rect:
                return False

            input_x, input_y = self._get_safe_coordinates(rect.right - 200, rect.bottom - 80)

            pyautogui.click(input_x, input_y)
            time.sleep(0.1)
            return True

        except Exception as e:
            raise RuntimeError(f"点击消息输入区域失败: {e}")

    def click_send_button(self) -> bool:
        try:
            wechat_window = self.find_wechat_window()
            if not wechat_window:
                return False

            rect = wechat_window.BoundingRectangle
            if not rect:
                return False

            send_x, send_y = self._get_safe_coordinates(rect.right - 100, rect.bottom - 50)

            pyautogui.click(send_x, send_y)
            time.sleep(0.1)
            return True

        except Exception as e:
            raise RuntimeError(f"点击发送按钮失败: {e}")

    def _search_contact(self, contact_name: str) -> bool:
        try:
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(0.2)

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
        except Exception as e:
            raise RuntimeError(f"搜索联系人失败: {e}")

    def _prepare_message_area(self) -> bool:
        if not self.click_message_input_area():
            return False
        return True

    def _send_message_content(self, message: str, use_send_button: bool = False) -> bool:
        try:
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
        except Exception as e:
            raise RuntimeError(f"发送消息内容失败: {e}")

    def SendMsg(self, msg: str, who: str | None = None, use_send_button: bool = False) -> WxResponse:
        try:
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

            if not self._send_message_content(msg, use_send_button):
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
        try:
            for process in psutil.process_iter(['name']):
                if process.info['name'] and ('WeChat' in process.info['name'] or '微信' in process.info['name']):
                    return True
            return False
        except Exception as e:
            raise RuntimeError(f"检查微信运行状态失败: {e}")

    def SendFiles(self, filepath: str, who: str | None = None) -> WxResponse:
        try:
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

            if not os.path.exists(filepath):
                raise FileNotFoundError(f"路径不存在: {filepath}")

            filepath = os.path.abspath(filepath)

            self._set_clipboard_files([filepath])

            if not self.paste_text():
                return WxResponse.failure(
                    message="无法粘贴文件",
                    data={"operation": "paste_file", "filepath": filepath}
                )
            time.sleep(0.1)

            pyautogui.press('enter')

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
        except FileNotFoundError as e:
            return WxResponse.error(
                message=f"文件不存在: {e}",
                data={
                    "operation": "send_file",
                    "target": who or "当前聊天",
                    "filepath": filepath,
                    "error_type": "FileNotFoundError",
                    "timestamp": time.time()
                }
            )
        except Exception as e:
            return WxResponse.error(
                message=f"发送文件失败: {e}",
                data={
                    "operation": "send_file",
                    "target": who or "当前聊天",
                    "filepath": filepath,
                    "error_type": type(e).__name__,
                    "timestamp": time.time()
                }
            )

    def _set_clipboard_files(self, file_paths: list[str]) -> None:
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
    wx = WeChat4()
    result = wx.SendMsg("测试成功了！", "文件传输助手")
    print(f"发送结果: {result}")
