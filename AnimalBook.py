import wx
from SimpleBookSample import BaseicAnimalBook


class AnimalBook(BaseicAnimalBook):
    def __init__(self, parent, animal_name, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.m_class_name.SetLabel(self.__class__.__name__)
        self.m_staticText_name = animal_name
        self.m_value = 0
        self.m_initial_right = 50
        self.m_create_value = 30
        self.m_right = self.m_initial_right
        self.m_pos_x = None
        self.m_pos_y = None
        self.m_dc = None
        self.set_control()
        self.root_window = None
        self.m_name.SetValue(animal_name)

    def set_root_window(self, root_window):
        self.root_window = root_window


    def set_control(self):
        self.m_gauge_value.SetValue(self.m_value)
        self.m_slider_value.SetValue(self.m_create_value)
        self.m_textCtrl_value.SetValue(str(self.m_create_value))

        self.m_gauge_right.SetValue(self.m_right)
        self.m_slider_right.SetValue(self.m_initial_right)
        self.m_textCtrl_right.SetValue(str(self.m_initial_right))

    def paint(self, panel, x=None, y=None):
        dc = wx.PaintDC(panel)
        dc.SetPen(wx.Pen('blue'))

        if x is not None:
            self.m_pos_x = x
        if y is not None:
            self.m_pos_y = y

        dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0)))
        dc.DrawCircle(self.m_pos_x, self.m_pos_y, 10)
        pos1 = (self.m_pos_x, self.m_pos_y + 10)
        pos2 = (self.m_pos_x - 10, self.m_pos_y + 40)
        pos3 = (self.m_pos_x + 10, self.m_pos_y + 40)
        dc.SetBrush(wx.Brush(wx.Colour(0, 255, 0)))
        dc.DrawPolygonList([[pos1, pos2, pos3]])
        dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0)))
        dc.SetFont(wx.Font(wx.FontInfo(8)))

        dc.DrawText(self.m_name.GetValue(), self.m_pos_x - 20, self.m_pos_y + 45)

    def onValueChanged(self, event):
        self.m_create_value = self.m_slider_value.GetValue()
        self.set_control()

    def onRightChanged(self, event):
        self.m_initial_right = self.m_slider_right.GetValue()
        self.set_control()

    def onValueText(self, event):
        value = int(self.m_textCtrl_value.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        self.m_create_value = value
        self.set_control()

    def onRightText(self, event):
        value = int(self.m_textCtrl_right.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.m_initial_right = value
        self.set_control()

    def onAnimalNameChange(self, event):
        if self.root_window is not None:
            self.root_window.Refresh()
