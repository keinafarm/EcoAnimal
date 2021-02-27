import wx
from SimpleBookSample import MainFrame, SimpleBookPanel
from AnimalBook import AnimalBook

class Gui(MainFrame):
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

    def onPaint( self, event ):
        dc = wx.PaintDC(self.m_panel)
        dc.SetPen(wx.Pen('blue'))
        for i in range(5):
            for j in range(20):
                x = j*45+20
                y = i*80+20
                animal = self.animal_list[i*20+j]
                animal.paint( x, y, dc )

    def onExit( self, event ):
        self.Destroy()

    def onNext( self, event ):
        self.next_page()

    def onPrev( self, event ):
        self.prev_page()

    def next_page(self):
        for panel in self.animal_list:
            book = panel.m_simplebook
            last_page = book.GetPageCount()
            current_page = book.GetSelection()
            if current_page < last_page:
                book.ChangeSelection(current_page+1)

    def prev_page(self):
        for panel in self.animal_list:
            book = panel.m_simplebook
            current_page = book.GetSelection()
            if current_page > 0:
                book.ChangeSelection(current_page-1)



if __name__ == "__main__":
    app = wx.App()
    frame = Gui(None)
    frame.Show()
    app.MainLoop()
