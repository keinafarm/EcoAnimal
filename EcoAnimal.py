import wx
from SimpleBookSample import MainFrame, SimpleBookPanel


class EcoAnimal(MainFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bSizer_animal_list = wx.BoxSizer(wx.VERTICAL)

        self.animal_list = []
        for i in range(1,101):
            animal_name = "Animal{0}".format(str(i))
            animal = AnimalBook(self.m_scrolledWindow, animal_name, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,0)
            self.bSizer_animal_list.Add(animal, 1, wx.EXPAND | wx.ALL, 5)
            self.animal_list.append(animal)

        self.m_scrolledWindow.SetSizer(self.bSizer_animal_list)

class AnimalBook(SimpleBookPanel):
    def __init__(self, parent, animal_name, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.m_class_name.SetLabel(self.__class__.__name__)
        self.m_name.SetValue(animal_name)

if __name__ == "__main__":
    app = wx.App()
    frame = EcoAnimal(None)
    frame.Show()
    app.MainLoop()
