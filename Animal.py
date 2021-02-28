import wx
from SimpleBookSample import BaseicAnimalBook, DialogParameterSetting


class AnimalModel:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.initial_right = 50
        self.create_value = 30
        self.right = self.initial_right
        self.consumption = self.create_value - 5  # 消費量
        self.purchase_amount = self.consumption  # 購入量

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_value_color(self):
        if self.value > 255:
            green = 255
        else:
            green = self.value
        return 0, green, 128

    def get_right_color(self):
        if self.right > 255:
            red = 255
        else:
            red = self.right
        return red, 0, 128

    def reset(self):
        self.value = 0
        self.right = self.initial_right

    def buy(self):
        if self.purchase_amount < self.right:
            return self.purchase_amount
        else:
            return None  # 権利が足りなくて買えない

    def request(self, price):
        if self.value - self.consumption > price:
            return True
        else:
            return False

    def sell(self, price):
        self.value -= price
        self.right += price

    def settlement(self, price):
        self.value += price
        self.right -= price

    def production(self):
        self.value += self.create_value


class AnimalView(BaseicAnimalBook):
    def __init__(self, parent, model, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.model = model

        self.m_class_name.SetLabel(self.__class__.__name__)
        self.m_staticText_name = self.model.name
        self.m_pos_x = None
        self.m_pos_y = None
        self.set_control()
        self.root_window = None  # この設定はself.m_name.SetValueより前
        self.m_name.SetValue(self.model.name)

    def set_root_window(self, root_window):
        self.root_window = root_window

    def set_control(self):
        self.m_gauge_value.SetValue(self.model.value / 10)

        self.m_slider_value.SetValue(self.model.create_value)
        self.m_textCtrl_value.SetValue(str(self.model.create_value))

        self.m_gauge_right.SetValue(self.model.right / 5)

        self.m_slider_right.SetValue(self.model.initial_right)
        self.m_textCtrl_right.SetValue(str(self.model.initial_right))

        self.m_slider_purchase_amount.SetValue(self.model.purchase_amount)
        self.m_textCtrl_purchase_amount.SetValue(str(self.model.purchase_amount))

        self.m_slider_consumption.SetValue(self.model.consumption)
        self.m_textCtrl_consumption.SetValue(str(self.model.consumption))

    def paint(self, panel, x=None, y=None):
        dc = wx.PaintDC(panel)
        dc.SetPen(wx.Pen('blue'))

        if x is not None:
            self.m_pos_x = x
        if y is not None:
            self.m_pos_y = y
        red, green, blue = self.model.get_right_color()
        print("red={0}".format(red))
        dc.SetBrush(wx.Brush(wx.Colour(red, green, blue)))
        dc.DrawCircle(self.m_pos_x, self.m_pos_y, 10)
        pos1 = (self.m_pos_x, self.m_pos_y + 10)
        pos2 = (self.m_pos_x - 10, self.m_pos_y + 40)
        pos3 = (self.m_pos_x + 10, self.m_pos_y + 40)
        red, green, blue = self.model.get_value_color()
        dc.SetBrush(wx.Brush(wx.Colour(red, green, blue)))
        dc.DrawPolygonList([[pos1, pos2, pos3]])
        dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0)))
        dc.SetFont(wx.Font(wx.FontInfo(8)))

        dc.DrawText(self.m_name.GetValue(), self.m_pos_x - 20, self.m_pos_y + 45)

    def onValueChanged(self, event):
        self.model.create_value = self.m_slider_value.GetValue()
        self.set_control()

    def onRightChanged(self, event):
        self.model.initial_right = self.m_slider_right.GetValue()
        self.set_control()

    def onValueText(self, event):
        value = int(self.m_textCtrl_value.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        self.model.create_value = value
        self.set_control()

    def onRightText(self, event):
        value = int(self.m_textCtrl_right.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.model.initial_right = value
        self.set_control()

    def onPurchaseAmountChanged(self, event):
        self.model.purchase_amount = self.m_slider_purchase_amount.GetValue()
        self.set_control()

    def onConsumptionChanged(self, event):
        self.model.consumption = self.m_slider_consumption.GetValue()
        self.set_control()

    def onPurchaseAmountText(self, event):
        value = int(self.m_slider_purchase_amount.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.model.purchase_amount = value
        self.set_control()

    def onConsumptionText(self, event):
        value = int(self.m_textCtrl_consumption.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.model.consumption = value
        self.set_control()

    def onAnimalNameChange(self, event):
        self.model.set_name(self.m_name.GetValue())
        if self.root_window is not None:
            self.root_window.Refresh()

    def set_parameter(self, dialog):
        self.model.create_value = dialog.create_value
        self.model.initial_right = dialog.initial_right
        self.model.purchase_amount = dialog.purchase_amount
        self.model.consumption = dialog.consumption
        self.set_control()


class AnimalParameterSettingDialog(DialogParameterSetting):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_value = 10
        self.initial_right = 10
        self.purchase_amount = 10
        self.consumption = 10
        self.set_control()

    def set_control(self):
        self.m_slider_value.SetValue(self.create_value)
        self.m_slider_right.SetValue(self.initial_right)
        self.m_slider_purchase_amount.SetValue(self.purchase_amount)
        self.m_slider_consumption.SetValue(self.consumption)

        self.m_textCtrl_value.SetValue(str(self.create_value))
        self.m_textCtrl_right.SetValue(str(self.initial_right))
        self.m_textCtrl_purchase_amount.SetValue(str(self.purchase_amount))
        self.m_textCtrl_consumption.SetValue(str(self.consumption))

    def onValueChanged(self, event):
        self.create_value = self.m_slider_value.GetValue()
        self.set_control()

    def onRightChanged(self, event):
        self.initial_right = self.m_slider_right.GetValue()
        self.set_control()

    def onPurchaseAmountChanged(self, event):
        self.purchase_amount = self.m_slider_purchase_amount.GetValue()
        self.set_control()

    def onConsumptionChanged(self, event):
        self.consumption = self.m_slider_consumption.GetValue()
        self.set_control()

    def onValueText(self, event):
        value = int(self.m_textCtrl_value.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        self.create_value = value
        self.set_control()

    def onRightText(self, event):
        value = int(self.m_textCtrl_right.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.initial_right = value
        self.set_control()

    def onPurchaseAmountText(self, event):
        value = int(self.m_slider_purchase_amount.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.purchase_amount = value
        self.set_control()

    def onConsumptionText(self, event):
        value = int(self.m_textCtrl_consumption.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.consumption = value
        self.set_control()
