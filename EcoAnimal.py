import wx
from SimpleBookSample import MainFrame, SimpleBookPanel


class EcoAnimal(MainFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bSizer_animal_list = wx.BoxSizer(wx.VERTICAL)

        self.animal_list = []
        for i in range(1,10):
            animal = SimpleBookPanel(self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,0)
            self.bSizer_animal_list.Add(animal, 1, wx.EXPAND | wx.ALL, 5)
            self.animal_list.append(animal)

        self.m_scrolledWindow.SetSizer(self.bSizer_animal_list)


if __name__ == "__main__":
    app = wx.App()
    frame = EcoAnimal(None)
    frame.Show()
    app.MainLoop()
