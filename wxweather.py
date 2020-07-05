import wx

class WxWeather(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent=parent, title=title)
        self.panel = wx.Panel(self)
        self.Show()



if __name__ == '__main__':
    app = wx.App()
    frame = WxWeather(None, "Weather")
    app.MainLoop()
