from .noname import Frame_window

class window(Frame_window):
    def __init__(self, parent):
        super().__init__(parent)

    def on_size(self, event):
        print(event, self.Size)
        self.m_textCtrl4.SetSize(-1, -1, self.Size[0] - 15, -1)
        self.m_textCtrl41.SetSize(-1, -1, self.Size[0] - 15, -1)
