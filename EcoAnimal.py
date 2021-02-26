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
        event.Skip()

    def onPrev( self, event ):
        self.prev_page()
        event.Skip()

    def onPaint( self, event ):
        event.Skip()

    def next_page(self):
        for book in self.animal_list:
            last_page = book.GetPageCount()
            current_page = book.GetCurrentPage()
            if current_page < last_page:
                book.ChangeSelection(current_page+1)

    def prev_page(self):
        for book in self.animal_list:
            current_page = book.GetCurrentPage()
            if current_page > 1:
                book.ChangeSelection(current_page-1)


class AnimalBook(SimpleBookPanel):
    def __init__(self, parent, animal_name, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.m_class_name.SetLabel(self.__class__.__name__)
        self.m_name.SetValue(animal_name)
        self.m_staticText_name = animal_name

    def paint(self, x, y, dc):
        dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0)))
        dc.DrawCircle(x, y, 10)
        pos1 = (x, y + 10)
        pos2 = (x - 10, y + 40)
        pos3 = (x + 10, y + 40)
        dc.SetBrush(wx.Brush(wx.Colour(0, 255, 0)))
        dc.DrawPolygonList([[pos1, pos2, pos3]])
        dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0)))
        dc.SetFont(wx.Font(wx.FontInfo(8)))

        dc.DrawText(self.m_name.GetValue(), x-20,y+45)

if __name__ == "__main__":
    app = wx.App()
    frame = EcoAnimal(None)
    frame.Show()
    app.MainLoop()
