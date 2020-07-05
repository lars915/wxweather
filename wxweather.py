import wx

class WxWeather(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent=parent, title=title)
        self.panel = wx.Panel(self)

        sizer = wx.FlexGridSizer(2, 2, 10, 10)
        self.panel.SetSizer(sizer)
        button = wx.Button(self.panel, -1)
        button2 = wx.Button(self.panel, -1)
        button3 = wx.Button(self.panel, -1)
        button4 = wx.Button(self.panel, -1)

        sizer.Add(button)
        sizer.Add(button2)
        sizer.Add(button3)
        sizer.Add(button4)
        self.Show()



if __name__ == '__main__':
    app = wx.App()
    frame = WxWeather(None, "Weather")
    app.MainLoop()
