from .noname import Frame_window
from wx.lib.agw import pygauge as PG
import wx
from wx.core import KeyEvent, CommandEvent, SizeEvent, ActivateEvent

wx.Gauge = PG.PyGauge  # 将 wx.Gauge 篡改为 PyGauge 以实现特定样式的进度条


class window(Frame_window):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.id_Alt_E = wx.NewIdRef()
        self.RegisterHotKey(self.id_Alt_E, wx.MOD_ALT, ord("E"))
        self.Bind(wx.EVT_HOTKEY, self.Alt_E, id=self.id_Alt_E)

    def Alt_E(self, event: KeyEvent) -> None:
        self.m_textCtrl1.SetEditable(True)
        self.m_textCtrl1.Clear()
        self.m_textCtrl1.Paste()
        self.m_textCtrl1.SetEditable(False)
        self.m_textCtrl2.SetEditable(True)
        self.m_textCtrl2.Clear()
        self.m_textCtrl2.SetFocus()

    def on_size(self, event: SizeEvent) -> None:
        self.m_textCtrl1.SetSize(-1, -1, self.Size[0] - 15, -1)
        self.m_textCtrl2.SetSize(-1, -1, self.Size[0] - 15, -1)
        return super().on_size(event)

    def on_text(self, event: CommandEvent) -> None:
        return super().on_text(event)

    def on_key_down(self, event: KeyEvent) -> None:
        return super().on_key_down(event)

    def on_key_up(self, event: KeyEvent) -> None:
        if self.m_textCtrl1.GetValue() == self.m_textCtrl2.GetValue():
            self.m_textCtrl2.SetEditable(False)
        print(self.m_textCtrl2.GetValue())
        print(event.GetUnicodeKey())
        print(event.GetRawKeyFlags())
        return super().on_key_up(event)

    def on_char(self, event: KeyEvent) -> None:
        return super().on_char(event)

    def on_char_hook(self, event: KeyEvent) -> None:
        return super().on_char_hook(event)

    def on_activate(self, event: ActivateEvent) -> None:
        if event.GetActive():
            print(event)
        # return super().on_activate(event)

    def on_button_click(self, event: CommandEvent):
        
        return super().on_button_click(event)
