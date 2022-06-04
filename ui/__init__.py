import time
from .noname import Frame_window
from wx.lib.agw import pygauge as PG
import wx
from wx.core import KeyEvent, SizeEvent, ActivateEvent
import threading

wx.Gauge = PG.PyGauge  # 将 wx.Gauge 篡改为 PyGauge 以实现特定样式的进度条


class window(Frame_window):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.id_Alt_E = wx.NewIdRef()
        self.RegisterHotKey(self.id_Alt_E, wx.MOD_ALT, ord("E"))
        self.Bind(wx.EVT_HOTKEY, self.Alt_E, id=self.id_Alt_E)
        self.start = 0
        self.top = 0

    def Alt_E(self, event: KeyEvent) -> None:
        self.m_textCtrl1.SetEditable(True)
        self.m_textCtrl1.Clear()
        self.m_textCtrl1.Paste()
        self.m_textCtrl1.SetEditable(False)
        self.m_textCtrl2.SetEditable(True)
        self.m_textCtrl2.Clear()
        self.m_textCtrl2.SetFocus()
        time.sleep(0.5)
        self.m_textCtrl2.Bind(wx.EVT_KEY_DOWN, self.start_editing_event)

    def on_size(self, event: SizeEvent) -> None:
        self.m_textCtrl1.SetSize(-1, -1, self.Size[0] - 15, -1)
        self.m_textCtrl2.SetSize(-1, -1, self.Size[0] - 15, -1)
        return super().on_size(event)

    def on_key_up(self, event: KeyEvent) -> None:
        print(self.m_textCtrl2.GetValue())
        # print(event.GetUnicodeKey())
        # print(event.GetRawKeyFlags())
        return super().on_key_up(event)

    def on_activate(self, event: ActivateEvent) -> None:
        if event.GetActive():
            print(event)
        # return super().on_activate(event)

    def start_editing_event(self, event: KeyEvent):
        self.top = 1
        self.m_textCtrl2.Unbind(wx.EVT_KEY_DOWN, handler=self.start_editing_event)  # noqa
        self.m_textCtrl2.Bind(wx.EVT_KEY_UP, self.end_editing_event)
        print("Start")
        self.threading = Calculator(parent=self)
        self.threading.start()
        event.Skip()

    def end_editing_event(self, event: KeyEvent):
        if self.top:
            if self.m_textCtrl1.GetValue() == self.m_textCtrl2.GetValue():
                self.m_textCtrl2.Unbind(wx.EVT_KEY_UP, handler=self.end_editing_event)  # noqa
                self.m_textCtrl2.SetEditable(False)
                self.top = 0
                print("End")
                self.threading.stop()
        event.Skip()


class Calculator(threading.Thread):
    def __init__(self, parent: window) -> None:
        self.parent = parent
        self.start_time = 0.0
        self.end_time = 0
        self.state = 0
        super().__init__(name="Calculator", daemon=True)

    def run(self):
        while self.state:
            self.parent.m_button成绩1.SetLabelText(str("%.2f" % (time.time() - self.start_time)))  # noqa
            # self.parent.m_button成绩2.SetLabelText()
            # self.parent.m_button成绩3.SetLabelText()
            # self.parent.m_button今日1.SetLabelText()
            # self.parent.m_button今日2.SetLabelText()
            # self.parent.m_button今日3.SetLabelText()
            time.sleep(0.001)

    def start(self):
        self.start_time = time.time()
        self.state = 1
        super().start()

    def stop(self):
        self.state = 0
