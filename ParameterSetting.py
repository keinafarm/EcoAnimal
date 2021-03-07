from SimpleBookSample import DialogParameterSetting
import wx
import gettext

_ = gettext.gettext


############################################################
#
#   パラメータ設定のダイアログクラス
#   初期値も管理する
#
############################################################

class ParameterSetting(DialogParameterSetting):
    class SettingProperty:
        def __init__(self, obj, method, label, slider_min, slider_max):
            """
            設定項目の情報を保持する
            """
            self.obj = obj  # 設定するオブジェクト
            self.method = method  # 対応するModelオブジェクト上のプロパティ
            self.label = label
            self.slider_min = slider_min
            self.slider_max = slider_max
            self.slider = None
            self.textCtrl = None

        def onSliderChanged(self, event):
            setattr(self.obj, self.method, self.slider.GetValue())         # obj.method = self.slider.GetValue()
            self.set_control()

        def onTextFocus(self, event):
            self.onText(event)
            event.Skip()  # これ入れないと、二回目にカーソルが入れられない

        def onText(self, event):
            value = int(self.textCtrl.GetValue())
            if value > self.slider_max:
                value = self.slider_max
            elif value < self.slider_min:
                value = self.slider_min
            setattr(self.obj, self.method, value)          # obj.method = value
            self.set_control()

        def set_control(self):
            value = getattr(self.obj, self.method)          # value = obj.method
            self.slider.SetValue(value)
            self.textCtrl.SetValue(str(value))

    def __init__(self, parent, initializer, tips):
        """
        一括設定ダイアログ初期化
        :param parent: 親window
        :param initializer: 初期値設定関数
        """
        super().__init__(parent)
        self.m_staticText_tips.SetLabel(tips)
        self.initial_right = None
        self.create_value = None
        self.consumption = None
        self.purchase_amount = None
        initializer(self)

        self.setting_property_list = []
        self.parameters = 0
        self.append(self.SettingProperty(self, "initial_right", "権利初期値", 0, 100))
        self.append(self.SettingProperty(self, "create_value", "生産量", 0, 100))
        self.append(self.SettingProperty(self, "consumption", "購入量", 0, 100))
        self.append(self.SettingProperty(self, "purchase_amount", "消費量", 0, 100))

    def append(self, setting_property):
        self.parameters += 1
        row_pos = self.parameters + 1  # レイアウト上の行番号

        self.m_staticText91 = wx.StaticText(self, wx.ID_ANY, setting_property.label, wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText91.Wrap(-1)

        self.m_staticText91.SetFont(
            wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.m_gbSizer.Add(self.m_staticText91, wx.GBPosition(row_pos, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        # 「利幅」テキスト入力
        setting_property.textCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(25, 12),
                                                wx.TE_PROCESS_ENTER)
        setting_property.textCtrl.SetFont(
            wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        setting_property.textCtrl.SetMinSize(wx.Size(25, 12))

        self.m_gbSizer.Add(setting_property.textCtrl, wx.GBPosition(row_pos, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        # 「利幅」スライダー
        setting_property.slider = wx.Slider(self, wx.ID_ANY, 50, setting_property.slider_min,
                                            setting_property.slider_max,
                                            wx.DefaultPosition, wx.Size(-1, 10), wx.SL_HORIZONTAL | wx.SL_SELRANGE)

        setting_property.slider.SetFont(
            wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        setting_property.slider.SetForegroundColour(wx.Colour(255, 0, 0))
        setting_property.slider.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        setting_property.slider.SetMinSize(wx.Size(-1, 10))

        self.m_gbSizer.Add(setting_property.slider, wx.GBPosition(row_pos, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        # 「利幅」イベント
        setting_property.textCtrl.Bind(wx.EVT_KILL_FOCUS, setting_property.onTextFocus)
        setting_property.textCtrl.Bind(wx.EVT_TEXT_ENTER, setting_property.onText)
        setting_property.slider.Bind(wx.EVT_SLIDER, setting_property.onSliderChanged)

        self.setting_property_list.append(setting_property)

    def set_control(self):
        for setting in self.setting_property_list:
            setting.set_control()

    def initialize_complete(self):
        """
        コンストラクタの終了
        ダイアログを確定する
        :return:
        """
        self.button_cancel = wx.Button(self, wx.ID_CANCEL, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_gbSizer.Add(self.button_cancel, wx.GBPosition(10, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.button_ok = wx.Button(self, wx.ID_OK, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_gbSizer.Add(self.button_ok, wx.GBPosition(10, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.button_cancel.Bind(wx.EVT_BUTTON, self.onCancel)
        self.button_ok.Bind(wx.EVT_BUTTON, self.onOk)

    def onCancel( self, event ):
        event.Skip()

    def onOk( self, event ):
        event.Skip()
