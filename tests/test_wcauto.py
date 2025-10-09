"""
wcauto 库的简单测试
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# 添加当前目录到路径，以便导入wcauto模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wcauto import WeChatBot


class TestWeChatBot(unittest.TestCase):
    """WeChatBot类的测试用例"""
    
    def setUp(self):
        """测试前的设置"""
        self.bot = WeChatBot()
    
    def test_init(self):
        """测试初始化"""
        bot = WeChatBot(
            search_delay=1.0,
            input_delay=0.2,
            send_delay=0.3,
            use_send_button=True,
            safe_mode=False
        )
        
        self.assertEqual(bot.search_delay, 1.0)
        self.assertEqual(bot.input_delay, 0.2)
        self.assertEqual(bot.send_delay, 0.3)
        self.assertEqual(bot.use_send_button, True)
        self.assertEqual(bot.safe_mode, False)
        self.assertEqual(bot.safe_mode_delay, 0)
    
    @patch('wcauto.wcauto.pyperclip.copy')
    def test_copy_to_clipboard_success(self, mock_copy):
        """测试成功复制到剪贴板"""
        mock_copy.return_value = None
        
        result = self.bot.copy_to_clipboard("test text")
        
        self.assertTrue(result)
        mock_copy.assert_called_once_with("test text")
    
    @patch('wcauto.wcauto.pyperclip.copy')
    def test_copy_to_clipboard_failure(self, mock_copy):
        """测试复制到剪贴板失败"""
        mock_copy.side_effect = Exception("Copy failed")
        
        result = self.bot.copy_to_clipboard("test text")
        
        self.assertFalse(result)
    
    @patch('wcauto.wcauto.pyautogui.hotkey')
    def test_paste_text_success(self, mock_hotkey):
        """测试成功粘贴文本"""
        mock_hotkey.return_value = None
        
        result = self.bot.paste_text()
        
        self.assertTrue(result)
        mock_hotkey.assert_called_once_with('ctrl', 'v')
    
    @patch('wcauto.wcauto.psutil.process_iter')
    def test_check_wechat_running_true(self, mock_process_iter):
        """测试微信正在运行的情况"""
        mock_process = MagicMock()
        mock_process.info = {'name': 'WeChat.exe'}
        mock_process_iter.return_value = [mock_process]
        
        result = self.bot.check_wechat_running()
        
        self.assertTrue(result)
    
    @patch('wcauto.wcauto.psutil.process_iter')
    def test_check_wechat_running_false(self, mock_process_iter):
        """测试微信未运行的情况"""
        mock_process = MagicMock()
        mock_process.info = {'name': 'OtherProcess.exe'}
        mock_process_iter.return_value = [mock_process]
        
        result = self.bot.check_wechat_running()
        
        self.assertFalse(result)
    
    def test_send_msg_compatibility(self):
        """测试SendMsg方法的兼容性"""
        with patch.object(self.bot, 'send_message', return_value=True) as mock_send:
            result = self.bot.SendMsg("test contact", "test message", True)
            
            self.assertTrue(result)
            mock_send.assert_called_once_with("test contact", "test message", True)


if __name__ == '__main__':
    unittest.main()