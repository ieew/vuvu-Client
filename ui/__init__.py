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
        self.id_CTRL_E = wx.NewIdRef()
        self.RegisterHotKey(self.id_CTRL_E, wx.MOD_CMD, ord("E"))
        self.Bind(wx.EVT_HOTKEY, self.Alt_E, id=self.id_CTRL_E)
        self.start = 0
        self.top = 0
        self.keystrokes = 0

    def Alt_E(self, event: KeyEvent) -> None:
        self.m_textCtrl1.SetEditable(True)
        self.m_textCtrl1.Clear()
        self.m_textCtrl1.Paste()
        self.m_textCtrl1.SetEditable(False)
        self.m_textCtrl2.SetEditable(True)
        self.m_textCtrl2.Clear()
        time.sleep(0.2)
        self.m_textCtrl2.SetFocus()
        self.m_textCtrl2.Bind(wx.EVT_KEY_DOWN, self.start_editing_event)

    def on_size(self, event: SizeEvent) -> None:
        self.m_textCtrl1.SetSize(-1, -1, self.Size[0] - 15, -1)
        self.m_textCtrl2.SetSize(-1, -1, self.Size[0] - 15, -1)
        return super().on_size(event)

    def on_key_down(self, event: KeyEvent):
        if self.top:
            self.keystrokes += 1
        event.Skip()

    def on_key_up(self, event: KeyEvent) -> None:
        print(self.m_textCtrl2.GetValue())
        # print(event.GetUnicodeKey())
        # print(event.GetRawKeyFlags())
        event.Skip()

    def on_activate(self, event: ActivateEvent) -> None:
        if event.GetActive():
            if self.top:
                print(event)
                self.m_textCtrl2.SetFocus()
        event.Skip()

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
                self.keystrokes = 0
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
            t = time.time() - self.start_time
            self.parent.m_button成绩1.SetLabelText("%.2f" % (len(self.parent.m_textCtrl2.GetValue()) / t * 60))  # noqa
            self.parent.m_button成绩2.SetLabelText("%.2f" % (self.parent.keystrokes / t))
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
