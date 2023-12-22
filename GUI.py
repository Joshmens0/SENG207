import wx

class Window:
    def __init__(self) :
        App=wx.App()
        self.WindowFrame()
        App.MainLoop()
    def WindowFrame(self):
        Frame=wx.Frame()
        Frame.Create(parent=None,title="Generator",size=wx.Size(450,300),style=2)
        Frame.Show()


        