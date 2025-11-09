import time
from wcauto import WeChat


wx = WeChat()
time.sleep(5)

wx.send_msg("你好", "文件传输助手")

time.sleep(5)
