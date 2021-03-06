# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"EcoAnimal"), pos = wx.DefaultPosition, size = wx.Size( 1227,698 ), style = wx.CAPTION|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.m_menubar = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menuItem_save = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"保存"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menuItem_save )

        self.m_menuItem_load = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"読み出し"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menuItem_load )

        self.m_menu_file.AppendSeparator()

        self.m_menuItem11 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"ログデータ保存"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menuItem11 )

        self.m_menu_file.AppendSeparator()

        self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"終了"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menuItem_exit )

        self.m_menubar.Append( self.m_menu_file, _(u"ファイル") )

        self.m_menu_run = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu_run, wx.ID_ANY, _(u"取引"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_run.Append( self.m_menuItem5 )

        self.m_menuItem_trade_run = wx.MenuItem( self.m_menu_run, wx.ID_ANY, _(u"連続取引開始"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_run.Append( self.m_menuItem_trade_run )

        self.m_menuItem_trade_stop = wx.MenuItem( self.m_menu_run, wx.ID_ANY, _(u"連続取引停止"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_run.Append( self.m_menuItem_trade_stop )

        self.m_menu_run.AppendSeparator()

        self.m_menuItem_10times = wx.MenuItem( self.m_menu_run, wx.ID_ANY, _(u"10回取引"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_run.Append( self.m_menuItem_10times )

        self.m_menuItem_50times = wx.MenuItem( self.m_menu_run, wx.ID_ANY, _(u"50回取引"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_run.Append( self.m_menuItem_50times )

        self.m_menubar.Append( self.m_menu_run, _(u"実行") )

        self.m_menu_BookList = wx.Menu()
        self.m_menuItem_next = wx.MenuItem( self.m_menu_BookList, wx.ID_ANY, _(u"次のページ"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_BookList.Append( self.m_menuItem_next )

        self.m_menuItem_prev = wx.MenuItem( self.m_menu_BookList, wx.ID_ANY, _(u"前のページ"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_BookList.Append( self.m_menuItem_prev )

        self.m_menu_BookList.AppendSeparator()

        self.m_menuItem_parameter_setting = wx.MenuItem( self.m_menu_BookList, wx.ID_ANY, _(u"一括設定"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_BookList.Append( self.m_menuItem_parameter_setting )

        self.m_menuItem4 = wx.MenuItem( self.m_menu_BookList, wx.ID_ANY, _(u"初期値に戻す"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_BookList.Append( self.m_menuItem4 )

        self.m_menubar.Append( self.m_menu_BookList, _(u"アニマル") )

        self.SetMenuBar( self.m_menubar )

        self.bSizer_animal_list = wx.GridBagSizer( 0, 0 )
        self.bSizer_animal_list.SetFlexibleDirection( wx.BOTH )
        self.bSizer_animal_list.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel.SetMinSize( wx.Size( 900,400 ) )

        self.bSizer_animal_list.Add( self.m_panel, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

        self.m_scrolledWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 280,-1 ), wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow.SetScrollRate( 5, 5 )
        self.m_scrolledWindow.SetMinSize( wx.Size( 280,400 ) )

        self.bSizer_animal_list.Add( self.m_scrolledWindow, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

        self.m_textCtrl_log = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl_log.SetMinSize( wx.Size( 1190,200 ) )

        self.bSizer_animal_list.Add( self.m_textCtrl_log, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )


        self.SetSizer( self.bSizer_animal_list )
        self.Layout()
        self.m_timer = wx.Timer()
        self.m_timer.SetOwner( self, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onSave, id = self.m_menuItem_save.GetId() )
        self.Bind( wx.EVT_MENU, self.onLoad, id = self.m_menuItem_load.GetId() )
        self.Bind( wx.EVT_MENU, self.onLogSave, id = self.m_menuItem11.GetId() )
        self.Bind( wx.EVT_MENU, self.onExit, id = self.m_menuItem_exit.GetId() )
        self.Bind( wx.EVT_MENU, self.onTrade, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_MENU, self.onTradeRun, id = self.m_menuItem_trade_run.GetId() )
        self.Bind( wx.EVT_MENU, self.onTradeStop, id = self.m_menuItem_trade_stop.GetId() )
        self.Bind( wx.EVT_MENU, self.on10times, id = self.m_menuItem_10times.GetId() )
        self.Bind( wx.EVT_MENU, self.on50times, id = self.m_menuItem_50times.GetId() )
        self.Bind( wx.EVT_MENU, self.onNext, id = self.m_menuItem_next.GetId() )
        self.Bind( wx.EVT_MENU, self.onPrev, id = self.m_menuItem_prev.GetId() )
        self.Bind( wx.EVT_MENU, self.onParameterSetting, id = self.m_menuItem_parameter_setting.GetId() )
        self.Bind( wx.EVT_MENU, self.onReset, id = self.m_menuItem4.GetId() )
        self.m_panel.Bind( wx.EVT_PAINT, self.onPaint )
        self.m_panel.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_textCtrl_log.Bind( wx.EVT_RIGHT_UP, self.onRightUpLogText )
        self.Bind( wx.EVT_TIMER, self.onTimer, id=wx.ID_ANY )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onSave( self, event ):
        event.Skip()

    def onLoad( self, event ):
        event.Skip()

    def onLogSave( self, event ):
        event.Skip()

    def onExit( self, event ):
        event.Skip()

    def onTrade( self, event ):
        event.Skip()

    def onTradeRun( self, event ):
        event.Skip()

    def onTradeStop( self, event ):
        event.Skip()

    def on10times( self, event ):
        event.Skip()

    def on50times( self, event ):
        event.Skip()

    def onNext( self, event ):
        event.Skip()

    def onPrev( self, event ):
        event.Skip()

    def onParameterSetting( self, event ):
        event.Skip()

    def onReset( self, event ):
        event.Skip()

    def onPaint( self, event ):
        event.Skip()

    def onRightUp( self, event ):
        event.Skip()

    def onRightUpLogText( self, event ):
        event.Skip()

    def onTimer( self, event ):
        event.Skip()


###########################################################################
## Class BaseicAnimalBook
###########################################################################

class BaseicAnimalBook ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 260,90 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetMinSize( wx.Size( 260,90 ) )
        self.SetMaxSize( wx.Size( 271,103 ) )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_simplebook = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_panel_page1 = wx.Panel( self.m_simplebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText4 = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"名前"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_name = wx.TextCtrl( self.m_panel_page1, wx.ID_ANY, _(u"アニマル名"), wx.DefaultPosition, wx.Size( -1,15 ), wx.TE_PROCESS_ENTER )
        self.m_name.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"価値"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText5, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_gauge_value = wx.Gauge( self.m_panel_page1, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 160,10 ), wx.GA_HORIZONTAL )
        self.m_gauge_value.SetValue( 0 )
        self.m_gauge_value.SetBackgroundColour( wx.Colour( 128, 255, 0 ) )
        self.m_gauge_value.SetMinSize( wx.Size( 160,10 ) )

        gbSizer1.Add( self.m_gauge_value, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"権利"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText7, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_gauge_right = wx.Gauge( self.m_panel_page1, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 160,10 ), wx.GA_HORIZONTAL )
        self.m_gauge_right.SetValue( 0 )
        self.m_gauge_right.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_gauge_right.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_gauge_right.SetMinSize( wx.Size( 160,10 ) )

        gbSizer1.Add( self.m_gauge_right, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

        self.m_class_name = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_class_name.Wrap( -1 )

        self.m_class_name.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_class_name, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText_value = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.Size( -1,10 ), wx.ALIGN_RIGHT )
        self.m_staticText_value.Wrap( -1 )

        self.m_staticText_value.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText_value.SetMinSize( wx.Size( 20,10 ) )

        gbSizer1.Add( self.m_staticText_value, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText_right = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.Size( 20,10 ), wx.ALIGN_RIGHT )
        self.m_staticText_right.Wrap( -1 )

        self.m_staticText_right.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText_right.SetMinSize( wx.Size( 20,10 ) )

        gbSizer1.Add( self.m_staticText_right, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.m_panel_page1.SetSizer( gbSizer1 )
        self.m_panel_page1.Layout()
        gbSizer1.Fit( self.m_panel_page1 )
        self.m_simplebook.AddPage( self.m_panel_page1, _(u"a page"), False )
        self.m_panel_page2 = wx.Panel( self.m_simplebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gbSizer2 = wx.GridBagSizer( 2, 2 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText8 = wx.StaticText( self.m_panel_page2, wx.ID_ANY, _(u"生産量"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText8, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_slider_create_value = wx.Slider( self.m_panel_page2, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL|wx.SL_SELRANGE )
        self.m_slider_create_value.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_slider_create_value.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
        self.m_slider_create_value.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_slider_create_value.SetMinSize( wx.Size( -1,10 ) )

        gbSizer2.Add( self.m_slider_create_value, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel_page2, wx.ID_ANY, _(u"権利初期値"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText9, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_slider_initial_right = wx.Slider( self.m_panel_page2, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL|wx.SL_SELRANGE )
        self.m_slider_initial_right.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_slider_initial_right.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        self.m_slider_initial_right.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_slider_initial_right.SetMinSize( wx.Size( -1,10 ) )

        gbSizer2.Add( self.m_slider_initial_right, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel_page2, wx.ID_ANY, _(u"２ページ目"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        self.m_staticText10.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText_name = wx.StaticText( self.m_panel_page2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_name.Wrap( -1 )

        self.m_staticText_name.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText_name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl_create_value = wx.TextCtrl( self.m_panel_page2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,12 ), wx.TE_PROCESS_ENTER )
        self.m_textCtrl_create_value.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_textCtrl_create_value.SetMinSize( wx.Size( 25,12 ) )

        gbSizer2.Add( self.m_textCtrl_create_value, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl_initial_right = wx.TextCtrl( self.m_panel_page2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,12 ), wx.TE_PROCESS_ENTER )
        self.m_textCtrl_initial_right.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_textCtrl_initial_right.SetMinSize( wx.Size( 25,12 ) )

        gbSizer2.Add( self.m_textCtrl_initial_right, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.m_panel_page2.SetSizer( gbSizer2 )
        self.m_panel_page2.Layout()
        gbSizer2.Fit( self.m_panel_page2 )
        self.m_simplebook.AddPage( self.m_panel_page2, _(u"a page"), False )
        self.m_panel_page3 = wx.Panel( self.m_simplebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gbSizer21 = wx.GridBagSizer( 2, 2 )
        gbSizer21.SetFlexibleDirection( wx.BOTH )
        gbSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText81 = wx.StaticText( self.m_panel_page3, wx.ID_ANY, _(u"購入量"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )

        self.m_staticText81.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer21.Add( self.m_staticText81, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_slider_purchase_amount = wx.Slider( self.m_panel_page3, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL|wx.SL_SELRANGE )
        self.m_slider_purchase_amount.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_slider_purchase_amount.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
        self.m_slider_purchase_amount.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_slider_purchase_amount.SetMinSize( wx.Size( -1,10 ) )

        gbSizer21.Add( self.m_slider_purchase_amount, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText91 = wx.StaticText( self.m_panel_page3, wx.ID_ANY, _(u"消費量"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91.Wrap( -1 )

        self.m_staticText91.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer21.Add( self.m_staticText91, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_slider_consumption = wx.Slider( self.m_panel_page3, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL|wx.SL_SELRANGE )
        self.m_slider_consumption.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_slider_consumption.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        self.m_slider_consumption.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_slider_consumption.SetMinSize( wx.Size( -1,10 ) )

        gbSizer21.Add( self.m_slider_consumption, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText101 = wx.StaticText( self.m_panel_page3, wx.ID_ANY, _(u"3ページ目"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText101.Wrap( -1 )

        self.m_staticText101.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer21.Add( self.m_staticText101, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText_name1 = wx.StaticText( self.m_panel_page3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_name1.Wrap( -1 )

        self.m_staticText_name1.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer21.Add( self.m_staticText_name1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl_purchase_amount = wx.TextCtrl( self.m_panel_page3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,12 ), wx.TE_PROCESS_ENTER )
        self.m_textCtrl_purchase_amount.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_textCtrl_purchase_amount.SetMinSize( wx.Size( 25,12 ) )

        gbSizer21.Add( self.m_textCtrl_purchase_amount, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl_consumption = wx.TextCtrl( self.m_panel_page3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,12 ), wx.TE_PROCESS_ENTER )
        self.m_textCtrl_consumption.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_textCtrl_consumption.SetMinSize( wx.Size( 25,12 ) )

        gbSizer21.Add( self.m_textCtrl_consumption, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.m_panel_page3.SetSizer( gbSizer21 )
        self.m_panel_page3.Layout()
        gbSizer21.Fit( self.m_panel_page3 )
        self.m_simplebook.AddPage( self.m_panel_page3, _(u"a page"), False )

        bSizer6.Add( self.m_simplebook, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        # Connect Events
        self.Bind( wx.EVT_LEFT_DCLICK, self.onAnimalClick )
        self.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_simplebook.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_panel_page1.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_staticText4.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_name.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_name.Bind( wx.EVT_TEXT, self.onAnimalNameChange )
        self.m_name.Bind( wx.EVT_TEXT_ENTER, self.onAnimalNameChange )
        self.m_staticText5.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_gauge_value.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_staticText7.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_gauge_right.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_class_name.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_staticText_value.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_staticText_right.Bind( wx.EVT_RIGHT_UP, self.onRightUp )
        self.m_slider_create_value.Bind( wx.EVT_SLIDER, self.onCreateValueChanged )
        self.m_slider_initial_right.Bind( wx.EVT_SLIDER, self.onInitialRightChanged )
        self.m_textCtrl_create_value.Bind( wx.EVT_KILL_FOCUS, self.onCreateValueTextFocus )
        self.m_textCtrl_create_value.Bind( wx.EVT_TEXT_ENTER, self.onCreateValueText )
        self.m_textCtrl_initial_right.Bind( wx.EVT_KILL_FOCUS, self.onInitialRightTextFocus )
        self.m_textCtrl_initial_right.Bind( wx.EVT_TEXT_ENTER, self.onInitialRightText )
        self.m_slider_purchase_amount.Bind( wx.EVT_SLIDER, self.onPurchaseAmountChanged )
        self.m_slider_consumption.Bind( wx.EVT_SLIDER, self.onConsumptionChanged )
        self.m_textCtrl_purchase_amount.Bind( wx.EVT_KILL_FOCUS, self.onPurchaseAmountTextFocus )
        self.m_textCtrl_purchase_amount.Bind( wx.EVT_TEXT_ENTER, self.onPurchaseAmountText )
        self.m_textCtrl_consumption.Bind( wx.EVT_KILL_FOCUS, self.onConsumptionTextFocus )
        self.m_textCtrl_consumption.Bind( wx.EVT_TEXT_ENTER, self.onConsumptionText )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onAnimalClick( self, event ):
        event.Skip()

    def onRightUp( self, event ):
        event.Skip()





    def onAnimalNameChange( self, event ):
        event.Skip()









    def onCreateValueChanged( self, event ):
        event.Skip()

    def onInitialRightChanged( self, event ):
        event.Skip()

    def onCreateValueTextFocus( self, event ):
        event.Skip()

    def onCreateValueText( self, event ):
        event.Skip()

    def onInitialRightTextFocus( self, event ):
        event.Skip()

    def onInitialRightText( self, event ):
        event.Skip()

    def onPurchaseAmountChanged( self, event ):
        event.Skip()

    def onConsumptionChanged( self, event ):
        event.Skip()

    def onPurchaseAmountTextFocus( self, event ):
        event.Skip()

    def onPurchaseAmountText( self, event ):
        event.Skip()

    def onConsumptionTextFocus( self, event ):
        event.Skip()

    def onConsumptionText( self, event ):
        event.Skip()


###########################################################################
## Class DialogParameterSetting
###########################################################################

class DialogParameterSetting ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"パラメータ設定"), pos = wx.DefaultPosition, size = wx.Size( 266,299 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_gbSizer = wx.GridBagSizer( 2, 2 )
        self.m_gbSizer.SetFlexibleDirection( wx.BOTH )
        self.m_gbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText_tips = wx.StaticText( self, wx.ID_ANY, _(u"全アニマルのパラメータを設定します"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_tips.Wrap( -1 )

        self.m_staticText_tips.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        self.m_gbSizer.Add( self.m_staticText_tips, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )


        self.SetSizer( self.m_gbSizer )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


