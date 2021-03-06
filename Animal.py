import wx
from SimpleBookSample import BaseicAnimalBook, DialogParameterSetting
import random
import pandas as pd
import matplotlib.pyplot as plt
from DataBase import DataBase


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
        DataBase.obj().set_object(index, self)
        self.reset()
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
        self.value = self.create_value
        self.right = self.initial_right
        self.history = pd.DataFrame(columns=['value', 'right'])

    def buy(self, animal_list, log):
        """
        買い取引
        :param animal_list: アニマルオブジェクトリスト
        :param log:ログ出力関数(msg)
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
        select = random.randint(0, length - 1)  # 取引先はランダムに選ぶ
        seller = seller_list[select][0]  # 売ってくれるAnimal
        right = seller_list[select][1]  # 価格
        seller.sell(self.purchase_amount, right)  # 取引を行う

        self.payment(self.purchase_amount, right)
        log("【{0}】は【{1}】から{2}で購入しました".format(self.name, seller.name, right))
        return "buy"

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

    def price(self, amount):
        """
        購入量を提示して、価格を得る
        :param amount: 購入量
        :return:[このオブジェクト,販売価格]
        """
        return [self, amount]  # とりあえず、量と価格は同じ

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
        self.history = self.history.append({'value': self.value, 'right': self.right}, ignore_index=True)

    #############
    #   グラフ表示
    #############
    def graph(self):
        """
        価値と権利の遷移をグラフで表示する
        :return:
        """
        self.history.plot()
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
        return DataBase.obj().get_name(self.index)

    @property
    def initial_right(self):
        return DataBase.obj().get_initial_right(self.index)

    @property
    def create_value(self):
        return DataBase.obj().get_create_value(self.index)

    @property
    def value(self):
        return DataBase.obj().get_value(self.index)

    @property
    def right(self):
        return DataBase.obj().get_right(self.index)

    @property
    def consumption(self):
        return DataBase.obj().get_consumption(self.index)

    @property
    def purchase_amount(self):
        return DataBase.obj().get_purchase_amount(self.index)

    #
    #   Setter
    #
    @name.setter
    def name(self, text):
        DataBase.obj().set_name(self.index, text)

    @initial_right.setter
    def initial_right(self, amount):
        DataBase.obj().set_initial_right(self.index, amount)

    @create_value.setter
    def create_value(self, amount):
        DataBase.obj().set_create_value(self.index, amount)

    @value.setter
    def value(self, amount):
        DataBase.obj().set_value(self.index, amount)

    @right.setter
    def right(self, amount):
        DataBase.obj().set_right(self.index, amount)

    @consumption.setter
    def consumption(self, amount):
        DataBase.obj().set_consumption(self.index, amount)

    @purchase_amount.setter
    def purchase_amount(self, amount):
        DataBase.obj().set_purchase_amount(self.index, amount)


############################################################
#
#   アニマルのユーザーインタフェース
#
############################################################
class AnimalView(BaseicAnimalBook):
    def __init__(self, parent, model, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id, pos, size, style, name)
        self.model = None  # データ管理部
        self.m_pos_x = None  # アイコン表示位置(X)
        self.m_pos_y = None  # アイコン表示位置(Y)
        self.root_window = None  # 最上位のView：この設定はself.m_name.SetValueより前
        self.set_model(model)  # データ管理部のデータを反映させる

    def set_model(self, model):
        """
        データ管理部のデータを反映させる
        :param model: データ管理部
        :return:
        """
        self.model = model
        self.m_class_name.SetLabel(model.__class__.__name__)  # クラス名
        self.m_staticText_name = self.model.name  # アニマル名
        self.set_full_control()  # 各パラメータを表示
        self.m_name.SetValue(self.model.name)

    def set_root_window(self, root_window):
        """
        最上位のView
        :param root_window:
        :return:
        """
        self.root_window = root_window

    #############
    #   BOOKパネル表示
    #############
    def set_full_control(self):
        """
        アニマルBook(左側の表示）の設定
        :return:
        """
        self.m_gauge_value.SetValue(self.model.value / 10)  # 価値のプログレスバー
        self.m_staticText_value.SetLabel(str(self.model.value))

        self.m_slider_create_value.SetValue(self.model.create_value)  # 生産量のスライダー
        self.m_textCtrl_create_value.SetValue(str(self.model.create_value))

        self.m_gauge_right.SetValue(self.model.right / 10)  # 権利のプログレスバー
        self.m_staticText_right.SetLabel(str(self.model.right))

        self.m_slider_initial_right.SetValue(self.model.initial_right)  # 権利の初期値のスライダー
        self.m_textCtrl_initial_right.SetValue(str(self.model.initial_right))

        self.m_slider_purchase_amount.SetValue(self.model.purchase_amount)  # 購入量のスライダー
        self.m_textCtrl_purchase_amount.SetValue(str(self.model.purchase_amount))

        self.m_slider_consumption.SetValue(self.model.consumption)  # 消費量のスライダー
        self.m_textCtrl_consumption.SetValue(str(self.model.consumption))

        self.set_control()

    def set_control(self):
        """
        アニマルBook(左側の表示）の設定 価値と権利だけ
        :return:
        """
        self.m_gauge_value.SetValue(self.model.value / 10)  # 価値のプログレスバー
        self.m_staticText_value.SetLabel(str(self.model.value))

        self.m_gauge_right.SetValue(self.model.right / 10)  # 権利のプログレスバー
        self.m_staticText_right.SetLabel(str(self.model.right))

    def set_parameter(self, dialog):
        """
        一括設定による設定
        :param dialog:
        :return:
        """
        self.model.set_parameter(dialog)
        self.set_full_control()

    #############
    #   アイコン表示
    #############
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
        line_length = self.model.value * 10 / 100
        if line_length > 20:
            line_length = 20
        dc.DrawLine(wx.Point(self.m_pos_x + 1, self.m_pos_y + 20),
                    wx.Point(self.m_pos_x + 1, self.m_pos_y + 20 - line_length))

        dc.SetPen(wx.Pen('red', width=3))
        line_length = self.model.right * 10 / 100
        if line_length > 20:
            line_length = 20
        dc.DrawLine(wx.Point(self.m_pos_x + 6, self.m_pos_y + 20),
                    wx.Point(self.m_pos_x + 6, self.m_pos_y + 20 - line_length))

        dc.DrawText(self.m_name.GetValue(), self.m_pos_x - 20, self.m_pos_y + 25)

    #############
    #   イベント処理
    #############
    def onCreateValueChanged(self, event):
        """
        BOOK:生産額スライダー変更
        :param event:
        :return:
        """
        self.model.create_value = self.m_slider_create_value.GetValue()
        self.set_full_control()

    def onCreateValueText(self, event):
        """
        BOOK:生産額テキストEnter
        :param event:
        :return:
        """
        value = int(self.m_textCtrl_create_value.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        self.model.create_value = value
        self.set_full_control()

    def onCreateValueTextFocus(self, event):
        """
        BOOK:生産額テキストフォーカスアウト
        :param event:
        :return:
        """
        self.onCreateValueText(event)
        event.Skip()  # これがないと、フォーカスがハズレない

    def onInitialRightChanged(self, event):
        """
        BOOK:権利初期値スライダー変更
        :param event:
        :return:
        """
        self.model.initial_right = self.m_slider_initial_right.GetValue()
        self.set_full_control()

    def onInitialRightText(self, event):
        """
        BOOK:権利初期値テキストEnter
        :param event:
        :return:
        """
        value = int(self.m_textCtrl_initial_right.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.model.initial_right = value
        self.set_full_control()

    def onInitialRightTextFocus(self, event):
        """
        BOOK:権利初期値テキストフォーカスアウト
        :param event:
        :return:
        """
        self.onInitialRightText(event)
        event.Skip()  # これがないと、フォーカスがハズレない

    def onPurchaseAmountChanged(self, event):
        """
        BOOK:取引量スライダー変更
        :param event:
        :return:
        """
        self.model.purchase_amount = self.m_slider_purchase_amount.GetValue()
        self.set_full_control()

    def onPurchaseAmountText(self, event):
        """
        BOOK:取引量テキストEnter
        :param event:
        :return:
        """
        value = int(self.m_textCtrl_purchase_amount.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.model.purchase_amount = value
        self.set_full_control()

    def onPurchaseAmountTextFocus(self, event):
        """
        BOOK:取引量テキストフォーカスアウト
        :param event:
        :return:
        """
        self.onPurchaseAmountText(event)
        event.Skip()

    def onConsumptionChanged(self, event):
        """
        BOOK:消費量スライダー変更
        :param event:
        :return:
        """
        self.model.consumption = self.m_slider_consumption.GetValue()
        self.set_full_control()

    def onConsumptionText(self, event):
        """
        BOOK:消費量テキストEnter
        :param event:
        :return:
        """
        value = int(self.m_textCtrl_consumption.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.model.consumption = value
        self.set_full_control()

    def onConsumptionTextFocus(self, event):
        """
        BOOK:消費量テキストフォーカスアウト
        :param event:
        :return:
        """
        self.onConsumptionText(event)
        event.Skip()

    def onAnimalNameChange(self, event):
        """
        BOOK:アニマル名変更
        :param event:
        :return:
        """
        self.model.name = self.m_name.GetValue()
        if self.root_window is not None:
            self.root_window.Refresh()

    def onRightUp(self, event):
        """
        https://python-minutes.blogspot.com/2017/01/pythongui.html
        :param event:
        :return:
        """
        menu = wx.Menu()
        item_1 = wx.MenuItem(menu, 1, 'パラメータ設定')
        item_2 = wx.MenuItem(menu, 2, 'グラフ')
        menu.Append(item_1)
        menu.Append(item_2)
        menu.Bind(wx.EVT_MENU, self.context_menu_select)

        self.PopupMenu(menu)

    def context_menu_select(self, event):
        menu_id = event.GetId()
        if menu_id == 1:
            self.parameter_setting()
        if menu_id == 2:
            self.model.graph()

    def load_property(self, obj):
        obj.initial_right = self.model.initial_right
        obj.create_value = self.model.create_value
        obj.consumption = self.model.consumption
        obj.purchase_amount = self.model.purchase_amount

    def parameter_setting(self):
        dialog = AnimalParameterSettingDialog(self, self.load_property, "{0}のパラメータを設定".format(self.model.name))
        result = dialog.ShowModal()
        if result != wx.ID_OK:
            return
        self.set_parameter(dialog)


############################################################
#
#   一括設定ダイアログのユーザーインタフェース
#
############################################################
class AnimalParameterSettingDialog(DialogParameterSetting):
    def __init__(self, parent, initializer, tips):
        """
        一括設定ダイアログ初期化
        :param parent: 親window
        :param initializer: 初期値設定関数
        """
        super().__init__(parent)
        self.m_staticText_tips = tips
        self.initial_right = None
        self.create_value = None
        self.consumption = None
        self.purchase_amount = None
        initializer(self)
        self.set_control()

    def set_control(self):
        self.m_slider_create_value.SetValue(self.create_value)
        self.m_slider_initial_right.SetValue(self.initial_right)
        self.m_slider_purchase_amount.SetValue(self.purchase_amount)
        self.m_slider_consumption.SetValue(self.consumption)

        self.m_textCtrl_create_value.SetValue(str(self.create_value))
        self.m_textCtrl_initial_right.SetValue(str(self.initial_right))
        self.m_textCtrl_purchase_amount.SetValue(str(self.purchase_amount))
        self.m_textCtrl_consumption.SetValue(str(self.consumption))

    def onValueChanged(self, event):
        self.create_value = self.m_slider_create_value.GetValue()
        self.set_control()

    def onRightChanged(self, event):
        self.initial_right = self.m_slider_initial_right.GetValue()
        self.set_control()

    def onPurchaseAmountChanged(self, event):
        self.purchase_amount = self.m_slider_purchase_amount.GetValue()
        self.set_control()

    def onConsumptionChanged(self, event):
        self.consumption = self.m_slider_consumption.GetValue()
        self.set_control()

    def onValueText(self, event):
        value = int(self.m_textCtrl_create_value.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        self.create_value = value
        self.set_control()

    def onValueTextFocus(self, event):
        self.onValueText(event)
        event.Skip()  # これ入れないと、二回目にカーソルが入れられない

    def onRightText(self, event):
        value = int(self.m_textCtrl_initial_right.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.initial_right = value
        self.set_control()

    def onRightTextFocus(self, event):
        self.onRightText(event)
        event.Skip()  # これ入れないと、二回目にカーソルが入れられない

    def onPurchaseAmountText(self, event):
        value = int(self.m_textCtrl_purchase_amount.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.purchase_amount = value
        self.set_control()

    def onPurchaseAmountTextFocus(self, event):
        self.onPurchaseAmountText(event)
        event.Skip()  # これ入れないと、二回目にカーソルが入れられない

    def onConsumptionText(self, event):
        value = int(self.m_textCtrl_consumption.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.consumption = value
        self.set_control()

    def onConsumptionTextFocus(self, event):
        self.onConsumptionText(event)
        event.Skip()  # これ入れないと、二回目にカーソルが入れられない
