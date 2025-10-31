import time
from wcauto import WeChat4


wx = WeChat4()
time.sleep(5)

wx.SendMsg("你好", "文件传输助手")

# wx.SendFiles(r"C:\Users\YangShengzhou\Desktop\杨圣洲-DevOps工程师.pdf", "文件传输助手")
