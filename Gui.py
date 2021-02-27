import wx
from SimpleBookSample import MainFrame
from AnimalBook import AnimalBookView


class Gui(MainFrame):
    def __init__(self, parent, model):
        super().__init__(parent)

        self.model = model
        animal_model_list = self.model.get_animal_list()
        self.bSizer_animal_list = wx.BoxSizer(wx.VERTICAL)

        self.animal_list = []
        for i in range(100):
            animal = AnimalBookView(self.m_scrolledWindow, animal_model_list[i], wx.ID_ANY, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
            self.bSizer_animal_list.Add(animal, 1, wx.EXPAND | wx.ALL, 5)
            self.animal_list.append(animal)
            animal.set_root_window(self)

        self.m_scrolledWindow.SetSizer(self.bSizer_animal_list)

    def logout(self, text):
        self.m_textCtrl.AppendText(text + '\n')

    def onPaint(self, event):
        for i in range(5):
            for j in range(20):
                x = j * 45 + 20
                y = i * 80 + 20
                animal = self.animal_list[i * 20 + j]
                animal.paint(self.m_panel, x, y)

    def onExit(self, event):
        self.Destroy()

    def onNext(self, event):
        self.next_page()

    def onPrev(self, event):
        self.prev_page()

    def next_page(self):
        for panel in self.animal_list:
            book = panel.m_simplebook
            last_page = book.GetPageCount()
            current_page = book.GetSelection()
            if current_page < last_page:
                book.ChangeSelection(current_page + 1)

    def prev_page(self):
        for panel in self.animal_list:
            book = panel.m_simplebook
            current_page = book.GetSelection()
            if current_page > 0:
                book.ChangeSelection(current_page - 1)

    def onRun(self, event):
        self.model.trade()

    def onReset(self, event):
        self.model.reset()
        self.Refresh()
