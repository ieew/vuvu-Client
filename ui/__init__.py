from .noname import Frame_window
import wx.lib.agw.pygauge as PG
import wx

wx.Gauge = PG.PyGauge  # 利用命名空间将 wx.Gauge 篡改为 PyGauge 以实现自定义的进度条


class window(Frame_window):
    def __init__(self, parent):
        super().__init__(parent)

    def on_size(self, event):
        self.m_textCtrl4.SetSize(-1, -1, self.Size[0] - 15, -1)
        self.m_textCtrl41.SetSize(-1, -1, self.Size[0] - 15, -1)
