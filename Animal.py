import wx
from SimpleBookSample import BaseicAnimalBook, DialogParameterSetting
import random
import pandas as pd


# https://qiita.com/ysdyt/items/9ccca82fc5b504e7913a
# https://aiacademy.jp/media/?p=152

class AnimalModel:
    animal_properties = None
    property_name_list = ['object', 'name', 'value', 'right', 'create_value', 'initial_right', 'consumption',
                          'purchase_amount']
    initial_values = {'object': None, 'name': None, 'right': 50, 'value': 30, 'create_value': 30, 'initial_right': 50,
                      'consumption': 30, 'purchase_amount': 30}

    @classmethod
    def init(cls, animals):
        cls.animal_properties = pd.DataFrame([cls.initial_values] * animals, columns=cls.property_name_list)

    @classmethod
    def set_initial_values(cls, initial_value):
        """
        全体の初期値を設定する
        :param initial_value: 初期値リスト（辞書型）
        :return:
        """
        cls.initial_values = initial_value

    @classmethod
    def load_property(cls, obj):
        obj.initial_right = cls.initial_values['initial_right']
        obj.create_value = cls.initial_values['create_value']
        obj.consumption = cls.initial_values['consumption']
        obj.purchase_amount = cls.initial_values['purchase_amount']

    @classmethod
    def store_property(cls, obj):
         cls.initial_values['initial_right'] = obj.initial_right
         cls.initial_values['create_value'] = obj.create_value
         cls.initial_values['consumption'] = obj.consumption
         cls.initial_values['purchase_amount'] = obj.purchase_amount


    def __init__(self, index, name):
        """
        アニマルを生成する
        :param index: index番号
        """
        self.index = index
        self.name = name
        AnimalModel.animal_properties.at[self.index, 'object'] = self
        self.value = self.create_value
        self.right = self.initial_right

    def set_parameter(self, dialog):
        self.create_value = dialog.create_value
        self.initial_right = dialog.initial_right
        self.purchase_amount = dialog.purchase_amount
        self.consumption = dialog.consumption
        #self.value = self.create_value
        #self.right = self.initial_right

    @property
    def name(self):
        return AnimalModel.animal_properties.at[self.index, 'name']

    @property
    def initial_right(self):
        return AnimalModel.animal_properties.at[self.index, 'initial_right']

    @property
    def create_value(self):
        return AnimalModel.animal_properties.at[self.index, 'create_value']

    @property
    def value(self):
        return AnimalModel.animal_properties.at[self.index, 'value']

    @property
    def right(self):
        return AnimalModel.animal_properties.at[self.index, 'right']

    @property
    def consumption(self):
        return AnimalModel.animal_properties.at[self.index, 'consumption']

    @property
    def purchase_amount(self):
        return AnimalModel.animal_properties.at[self.index, 'purchase_amount']

    @name.setter
    def name(self, text):
        AnimalModel.animal_properties.at[self.index, 'name'] = text

    @initial_right.setter
    def initial_right(self, amount):
        AnimalModel.animal_properties.at[self.index, 'initial_right'] = amount

    @create_value.setter
    def create_value(self, amount):
        AnimalModel.animal_properties.at[self.index, 'create_value'] = amount

    @value.setter
    def value(self, amount):
        AnimalModel.animal_properties.at[self.index, 'value'] = amount

    @right.setter
    def right(self, amount):
        AnimalModel.animal_properties.at[self.index, 'right'] = amount

    @consumption.setter
    def consumption(self, amount):
        AnimalModel.animal_properties.at[self.index, 'consumption'] = amount

    @purchase_amount.setter
    def purchase_amount(self, amount):
        AnimalModel.animal_properties.at[self.index, 'purchase_amount'] = amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def reset(self):
        self.value = 0
        self.right = self.initial_right

    def buy(self, animal_list, log):
        # 必要量を持っているところを探す
        seller_list = [animal for animal in animal_list if animal.request(self.purchase_amount)]
        length = len(seller_list)
        if length == 0:
            log("【{0}】は購入できませんでした".format(self.name))
            return "nobody"

        # 必要量を手持ちの金額で売ってくれるところを探す
        seller_list = [animal.price(self.purchase_amount) for animal in seller_list if
                       animal.price(self.purchase_amount)[1] <= self.right]
        length = len(seller_list)
        if length == 0:
            log("【{0}】は権利不足でした".format(self.name))
            return "shortage"

        select = random.randint(0, length - 1)
        seller = seller_list[select][0]
        right = seller_list[select][1]
        seller.sell(self.purchase_amount, right)

        self.settlement(self.purchase_amount, right)
        log("【{0}】は【{1}】から{2}で購入しました".format(self.name, seller.get_name(), right))
        return "buy"

    def price(self, amount):
        return [self, amount]  # とりあえず、量と価格は同じ

    def request(self, amount):
        if self.value - self.consumption >= amount:  # 売ったあと、自分の分は残っているか
            return True
        else:
            return False

    def sell(self, amount, right):
        self.value -= amount
        self.right += right

    def settlement(self, amount, right):
        self.value += amount
        self.right -= right

    def production(self):
        self.value += self.create_value

    def consume(self):
        self.value -= self.consumption
        if self.value < 0:
            self.value = 0


class AnimalView(BaseicAnimalBook):
    def __init__(self, parent, model, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.model = None
        self.m_pos_x = None
        self.m_pos_y = None
        self.root_window = None  # この設定はself.m_name.SetValueより前
        self.set_model(model)

    def set_model(self, model):
        self.model = model
        self.m_class_name.SetLabel(model.__class__.__name__)
        self.m_staticText_name = self.model.name
        self.set_control()
        self.m_name.SetValue(self.model.name)

    def set_root_window(self, root_window):
        self.root_window = root_window

    def set_control(self):
        self.m_gauge_value.SetValue(self.model.value / 10)
        self.m_staticText_value.SetLabel(str(self.model.value))

        self.m_slider_value.SetValue(self.model.create_value)
        self.m_textCtrl_value.SetValue(str(self.model.create_value))

        self.m_gauge_right.SetValue(self.model.right / 5)
        self.m_staticText_right.SetLabel(str(self.model.right))

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

        if self.model.right > 255:
            red = 255
        else:
            red = self.model.right
        green = 0
        blue = 200
        print("red={0}".format(red))
        dc.SetBrush(wx.Brush(wx.Colour(red, green, blue)))
        dc.DrawCircle(self.m_pos_x - 6, self.m_pos_y, 4)

        pos1 = (self.m_pos_x - 6, self.m_pos_y + 4)
        pos2 = (self.m_pos_x - 10, self.m_pos_y + 20)
        pos3 = (self.m_pos_x - 2, self.m_pos_y + 20)

        if self.model.value > 255:
            green = 255
        else:
            green = self.model.value
        red = 0
        blue = 200
        dc.SetBrush(wx.Brush(wx.Colour(red, green, blue)))
        dc.DrawPolygonList([[pos1, pos2, pos3]])
        dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0)))
        dc.SetFont(wx.Font(wx.FontInfo(8)))

        dc.SetPen(wx.Pen('green', width=3))
        line_length = self.model.value * 5 / 100
        if line_length > 20:
            line_length = 20
        dc.DrawLine(wx.Point(self.m_pos_x + 1, self.m_pos_y + 20),
                    wx.Point(self.m_pos_x + 1, self.m_pos_y + 20 - line_length))

        dc.SetPen(wx.Pen('red', width=3))
        line_length = self.model.right * 20 / 100
        if line_length > 20:
            line_length = 20
        dc.DrawLine(wx.Point(self.m_pos_x + 6, self.m_pos_y + 20),
                    wx.Point(self.m_pos_x + 6, self.m_pos_y + 20 - line_length))

        dc.DrawText(self.m_name.GetValue(), self.m_pos_x - 20, self.m_pos_y + 25)

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
        self.model.set_parameter(dialog)
        self.set_control()


class AnimalParameterSettingDialog(DialogParameterSetting):
    def __init__(self, parent, initializer):
        super().__init__(parent)
        self.initial_right = None
        self.create_value = None
        self.consumption = None
        self.purchase_amount = None
        initializer(self)
        self.set_control()

    def get_initial_value(self):
        values = {'create_value': self.create_value,
                  "initial_right": self.initial_right,
                  'consumption': self.consumption,
                  'purchase_amount': self.purchase_amount}
        return values

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
