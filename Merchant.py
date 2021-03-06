############################################################
#
#   商人：購入したものに利益を載せて販売する人
#
############################################################

from DataBase import DataBase
from Animal import AnimalModel, AnimalParameterSettingDialog, AnimalView
import wx
import gettext
_ = gettext.gettext

#############
#
#   全体のデータ管理オブジェクト
#
#############
class MerchantData(DataBase):
    def __init__(self):
        super().__init__()
        self.property_name_list.append('margin')
        self.initial_values['margin'] = 0

    def load_property(self, obj):
        super().load_property(obj)
        obj.margin = self.initial_values['margin']

    def store_property(self, obj):
        super().store_property(obj)
        self.initial_values['margin'] = obj.margin

    #############
    #   プロパティ Getter,setter
    #############
    #
    #   Getter
    #
    def get_margin(self, index):
        return self.animal_properties.at[index, 'margin']

    def set_margin(self, index, amount):
        self.animal_properties.at[index, 'margin'] = amount


#############
#
#   個別のデータ管理オブジェクト(Model)
#
#############
class MerchantModel(AnimalModel):
    def __init__(self, index, name):
        super().__init__(index, name)
        self.margin = 0

    def set_parameter(self, source):
        super().set_parameter(source)
        self.margin = source.margin

    def price(self, amount):
        """
        購入量を提示して、価格を得る
        :param amount: 購入量
        :return:[このオブジェクト,販売価格]
        """
        return [self, amount * (1 + self.margin / 100)]  # 価格はマージンを載せる

#############
#
#   個別のデータ設定オブジェクト(View)
#
#############
class MerchantView(AnimalView):
    def __init__(self, parent, model, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                     style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
            super().__init__(parent, model, id, pos, size, style, name)

    def load_property(self, obj):
        super().load_property(obj)
        obj.margin = self.model.margin

    def make_dialog(self):
        dialog = MerchantParameterSettingDialog(self, self.load_property, "{0}のパラメータを設定".format(self.model.name))
        return dialog

############################################################
#
#   設定ダイアログのユーザーインタフェース
#
############################################################

class MerchantParameterSettingDialog(AnimalParameterSettingDialog):
    def __init__(self, parent, initializer, tips):
        self.margin = None
        super().__init__(parent, initializer, tips)
        # 「利幅」ラベル
        self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, _(u"利幅"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91.Wrap( -1 )

        self.m_staticText91.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_gbSizer.Add( self.m_staticText91, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        # 「利幅」テキスト入力
        self.m_textCtrl_margin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,12 ), wx.TE_PROCESS_ENTER )
        self.m_textCtrl_margin.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_textCtrl_margin.SetMinSize( wx.Size( 25,12 ) )

        self.m_gbSizer.Add( self.m_textCtrl_margin, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        # 「利幅」スライダー
        self.m_slider_margin = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL|wx.SL_SELRANGE )

        self.m_slider_margin.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_slider_margin.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        self.m_slider_margin.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_slider_margin.SetMinSize( wx.Size( -1,10 ) )

        self.m_gbSizer.Add( self.m_slider_margin, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        # 「利幅」イベント
        self.m_textCtrl_margin.Bind( wx.EVT_KILL_FOCUS, self.onMarginTextFocus )
        self.m_textCtrl_margin.Bind( wx.EVT_TEXT_ENTER, self.onMarginText )
        self.m_slider_margin.Bind( wx.EVT_SLIDER, self.onMarginChanged )


    def set_control(self):
        super().set_control()
        self.m_slider_margin.SetValue(self.margin)
        self.m_textCtrl_margin.SetValue(str(self.margin))

    def onMarginChanged(self, event):
        self.margin = self.m_slider_margin.GetValue()
        self.set_control()

    def onMarginText(self, event):
        value = int(self.m_textCtrl_margin.GetValue())
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        self.margin = value
        self.set_control()

    def onMarginTextFocus(self, event):
        self.onMarginText(event)
        event.Skip()  # これ入れないと、二回目にカーソルが入れられない
