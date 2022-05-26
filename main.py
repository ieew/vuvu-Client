import wx
from ui.noname import window


app = wx.App()
frame = window(None)
frame.Show()
app.MainLoop()
