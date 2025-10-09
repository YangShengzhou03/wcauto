import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wcauto import WeChat

class TestWeChat(unittest.TestCase):
    def setUp(self):
        self.bot = WeChat()
    
    def test_init(self):
        bot = WeChat()
        self.assertIsNotNone(bot.screen_width)
        self.assertIsNotNone(bot.screen_height)
    
    @patch('wcauto.wcauto.pyperclip.copy')
    def test_copy_to_clipboard_success(self, mock_copy):
        mock_copy.return_value = None
        result = self.bot.copy_to_clipboard("test text")
        self.assertTrue(result)
        mock_copy.assert_called_once_with("test text")
    
    @patch('wcauto.wcauto.pyperclip.copy')
    def test_copy_to_clipboard_failure(self, mock_copy):
        mock_copy.side_effect = Exception("Copy failed")
        result = self.bot.copy_to_clipboard("test text")
        self.assertFalse(result)
    
    @patch('wcauto.wcauto.pyautogui.hotkey')
    def test_paste_text_success(self, mock_hotkey):
        mock_hotkey.return_value = None
        result = self.bot.paste_text()
        self.assertTrue(result)
        mock_hotkey.assert_called_once_with('ctrl', 'v')
    
    @patch('wcauto.wcauto.psutil.process_iter')
    def test_check_wechat_running_true(self, mock_process_iter):
        mock_process = MagicMock()
        mock_process.info = {'name': 'WeChat.exe'}
        mock_process_iter.return_value = [mock_process]
        result = self.bot.check_wechat_running()
        self.assertTrue(result)
    
    @patch('wcauto.wcauto.psutil.process_iter')
    def test_check_wechat_running_false(self, mock_process_iter):
        mock_process = MagicMock()
        mock_process.info = {'name': 'OtherProcess.exe'}
        mock_process_iter.return_value = [mock_process]
        result = self.bot.check_wechat_running()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()