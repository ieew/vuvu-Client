import wx
from ui import window


app = wx.App()
frame = window(None)
frame.Show()
app.MainLoop()
