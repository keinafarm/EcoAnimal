import wx
from SimpleBookSample import BaseicAnimalBook, DialogParameterSetting
import random
import pandas as pd
import matplotlib.pyplot as plt

# https://qiita.com/ysdyt/items/9ccca82fc5b504e7913a
# https://aiacademy.jp/media/?p=152

############################################################
#
#   アニマルのデータ管理
#
############################################################

class AnimalModel:
    #############
    #
    #   クラス変数
    #
    #############

    animal_properties = None
    property_name_list = ['object', 'name', 'value', 'right', 'create_value', 'initial_right', 'consumption',
                          'purchase_amount']
    initial_values = {'object': None, 'name': None, 'right': 50, 'value': 30, 'create_value': 30, 'initial_right': 50,
                      'consumption': 30, 'purchase_amount': 30}
    animal_count = 0

    #############
    #
    #   クラスメソッド
    #
    #############

    @classmethod
    def init(cls, animals):
        cls.animal_properties = pd.DataFrame([cls.initial_values] * animals, columns=cls.property_name_list)
        cls.animal_count = animals

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

    @classmethod
    def save(cls, pathname):
        save_list = cls.animal_properties.copy()
        save_list['object'] = None
        save_list.to_excel(pathname)

    @classmethod
    def load(cls, pathname):
        animal_list = pd.read_excel(pathname)
        if len(animal_list) != cls.animal_count:
            return "データ数は{0}です。(現在:{1})".format(cls.animal_count, len(animal_list))

        cls.animal_properties = animal_list
        return None

    #############
    #
    #   アニマルデータ管理オブジェクト
    #
    #############
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
        self.history = pd.DataFrame(columns=['value', 'right'])

    def set_parameter(self, source):
        """
        初期値を設定する
        :param source:
        :return:
        """
        self.create_value = source.create_value
        self.initial_right = source.initial_right
        self.purchase_amount = source.purchase_amount
        self.consumption = source.consumption

    def reset(self):
        """
        初期状態に戻す
        :return:
        """
        self.value = 0
        self.right = self.initial_right

    def buy(self, animal_list, log):
        """
        買い取引
        :param animal_list: アニマルオブジェクトリスト
        :param log(msg):ログ出力関数
        :return: 取引結果
        """
        # 必要量を持っているところを探す
        seller_list = [animal for animal in animal_list if animal.request(self.purchase_amount)]
        length = len(seller_list)
        if length == 0:
            log("【{0}】は購入できませんでした".format(self.name))
            return "nobody"

        # 必要量を手持ちの金額で売ってくれるところを探す
        seller_list = [animal.price(self.purchase_amount) for animal in seller_list if
                       animal.price(self.purchase_amount)[1] <= self.right]
                            # animal.price:オブジェクトと販売価格のリスト
        length = len(seller_list)
        if length == 0:
            log("【{0}】は権利不足でした".format(self.name))
            return "shortage"

        # 供給も手持ちも十分なので取引を行う
        select = random.randint(0, length - 1)          # 取引先はランダムに選ぶ
        seller = seller_list[select][0]                 # 売ってくれるAnimal
        right = seller_list[select][1]                  # 価格
        seller.sell(self.purchase_amount, right)        # 取引を行う

        self.payment(self.purchase_amount, right)
        log("【{0}】は【{1}】から{2}で購入しました".format(self.name, seller.name, right))
        return "buy"

    def price(self, amount):
        """
        購入量を提示して、価格を得る
        :param amount: 購入量
        :return:[このオブジェクト,販売価格]
        """
        return [self, amount]  # とりあえず、量と価格は同じ

    def request(self, amount):
        """
        購入量を提示して、販売可能かどうか問い合わせる
        :param amount:
        :return:True:必要量はある False:販売不可
        """
        if self.value - self.consumption >= amount:  # 売ったあと、自分の分は残っているか
            return True
        else:
            return False

    def sell(self, amount, right):
        """
        販売処理
        :param amount:販売量
        :param right:取得する権利量
        :return:
        """

        self.value -= amount
        self.right += right

    def payment(self, amount, right):
        """
        支払い
        :param amount:購入量
        :param right:支払いする権利量
        :return:
        """
        self.value += amount
        self.right -= right

    def production(self):
        """
        生産：一定期間毎に価値を生産する
        :return:
        """
        self.value += self.create_value

    def consume(self):
        """
        消費：一定期間毎に価値を消費する
        :return:
        """
        self.value -= self.consumption
        if self.value < 0:
            self.value = 0

    def memory(self):
        """
        価値と権利の値を記憶する
        :return:
        """
        self.history = self.history.append({'value':self.value,  'right':self.right}, ignore_index=True)

    #############
    #   グラフ表示
    #############
    def graph(self):
        self.history.plot()
        print(self.history)
        plt.title("{0}".format(self.name))
        plt.show()

    #############
    #   プロパティ Getter,setter
    #############
    #
    #   Getter
    #
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
    #
    #   Setter
    #
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


############################################################
#
#   アニマルのユーザーインタフェース
#
############################################################
class AnimalView(BaseicAnimalBook):
    def __init__(self, parent, model, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.model = None           # データ管理部
        self.m_pos_x = None         # アイコン表示位置(X)
        self.m_pos_y = None         # アイコン表示位置(Y)
        self.root_window = None     # 最上位のView：この設定はself.m_name.SetValueより前
        self.set_model(model)       # データ管理部のデータを反映させる

    def set_model(self, model):
        """
        データ管理部のデータを反映させる
        :param model: データ管理部
        :return:
        """
        self.model = model
        self.m_class_name.SetLabel(model.__class__.__name__)    # クラス名
        self.m_staticText_name = self.model.name                # アニマル名
        self.set_control()                                      # 各パラメータを表示
        self.m_name.SetValue(self.model.name)

    def set_root_window(self, root_window):
        """
        最上位のView
        :param root_window:
        :return:
        """
        self.root_window = root_window

    def set_control(self):
        """
        アニマルBook(左側の表示）の設定
        :return:
        """
        self.m_gauge_value.SetValue(self.model.value / 10)              # 価値のプログレスバー
        self.m_staticText_value.SetLabel(str(self.model.value))

        self.m_slider_value.SetValue(self.model.create_value)           # 生産量のスライダー
        self.m_textCtrl_value.SetValue(str(self.model.create_value))

        self.m_gauge_right.SetValue(self.model.right / 10)               # 権利のプログレスバー
        self.m_staticText_right.SetLabel(str(self.model.right))

        self.m_slider_right.SetValue(self.model.initial_right)          # 権利の初期値のスライダー
        self.m_textCtrl_right.SetValue(str(self.model.initial_right))

        self.m_slider_purchase_amount.SetValue(self.model.purchase_amount)  # 購入量のスライダー
        self.m_textCtrl_purchase_amount.SetValue(str(self.model.purchase_amount))

        self.m_slider_consumption.SetValue(self.model.consumption)      # 消費量のスライダー
        self.m_textCtrl_consumption.SetValue(str(self.model.consumption))

    def paint(self, panel, x=None, y=None):
        """
        アイコンを描画
        :param panel: 上位Vew
        :param x:始点(X)
        :param y:始点(Y)
        :return:
        """
        dc = wx.PaintDC(panel)
        dc.SetPen(wx.Pen('blue'))

        self.m_pos_x = x
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
        self.model.name = self.m_name.GetValue()
        if self.root_window is not None:
            self.root_window.Refresh()

    def set_parameter(self, dialog):
        self.model.set_parameter(dialog)
        self.set_control()

    def onRightUp(self, event):
        """
        https://python-minutes.blogspot.com/2017/01/pythongui.html
        :param event:
        :return:
        """
        menu = wx.Menu()
        item_1 = wx.MenuItem(menu, 1, 'グラフ')
        menu.Append(item_1)
        menu.Bind(wx.EVT_MENU, self.context_menu_select)

        self.PopupMenu(menu)

    def context_menu_select(self, event):
        id = event.GetId()
        print("Context Menu ID={0}".format(id))
        if id == 1:
            self.model.graph()

############################################################
#
#   一括設定ダイアログのユーザーインタフェース
#
############################################################
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

    def onValueTextForcus(self, event):
        self.onValueText(event)
        event.Skip()        # これ入れないと、二回目にカーソルが入れられない

    def onRightText(self, event):
        value = int(self.m_textCtrl_right.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.initial_right = value
        self.set_control()

    def onRightTextForcus(self, event):
        self.onRightText(event)
        event.Skip()        # これ入れないと、二回目にカーソルが入れられない

    def onPurchaseAmountText(self, event):
        value = int(self.m_textCtrl_purchase_amount.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.purchase_amount = value
        self.set_control()

    def onPurchaseAmountTextForcus(self, event):
        self.onPurchaseAmountText(event)
        event.Skip()        # これ入れないと、二回目にカーソルが入れられない

    def onConsumptionText(self, event):
        value = int(self.m_textCtrl_consumption.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.consumption = value
        self.set_control()

    def onConsumptionTextForcus(self, event):
        self.onConsumptionText(event)
        event.Skip()        # これ入れないと、二回目にカーソルが入れられない

