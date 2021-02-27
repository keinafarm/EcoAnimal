import wx
from Gui import Gui



if __name__ == "__main__":
    app = wx.App()
    frame = Gui(None)
    frame.Show()
    app.MainLoop()