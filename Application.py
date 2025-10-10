from wcauto import WeChat4

# wx = WeChat4()
# wx.SendMsg("文件传输", "文件传输助手")
wx = WeChat4()
print(wx.find_chrome_window_and_close())

# wx.SendFiles(r"C:\Users\YangShengzhou\Desktop\杨圣洲-DevOps工程师.pdf", "文件传输助手")
