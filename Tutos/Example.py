import wx

class MyFrame(wx.Frame):
    def __init__(self, parent=None, title=None):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title)
        self.panel = wx.Panel(self, size=(350, 450))
        # this sets up the painting canvas
        self.panel.Bind(wx.EVT_PAINT, self.on_paint)
        # set frame size to fit panel
        self.Fit()

    def on_paint(self, event):
        # establish the painting canvas
        dc = wx.PaintDC(self.panel)
        x = 0
        y = 0
        w, h = self.GetSize()
        dc.GradientFillLinear((x, y, w, h), 'blue', 'black')


app = wx.App(0)
MyFrame(title='Gradient Test').Show()
app.MainLoop()