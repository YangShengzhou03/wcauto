import time
from wcauto import WeChat


wx = WeChat()
time.sleep(5)

wx.send_msg("你好", "文件传输助手")

time.sleep(5)

wx.send_files(r"C:\Users\YangShengzhou\Desktop\杨圣洲-DevOps工程师.pdf", "文件传输助手")
