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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1227,698 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.m_menubar = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"終了"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menuItem_exit )

        self.m_menubar.Append( self.m_menu_file, _(u"File") )

        self.m_menu_BookList = wx.Menu()
        self.m_menuItem_next = wx.MenuItem( self.m_menu_BookList, wx.ID_ANY, _(u"次のページ"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_BookList.Append( self.m_menuItem_next )

        self.m_menuItem_prev = wx.MenuItem( self.m_menu_BookList, wx.ID_ANY, _(u"前のページ"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_BookList.Append( self.m_menuItem_prev )

        self.m_menubar.Append( self.m_menu_BookList, _(u"Book List") )

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

        self.m_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl.SetMinSize( wx.Size( 1190,200 ) )

        self.bSizer_animal_list.Add( self.m_textCtrl, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )


        self.SetSizer( self.bSizer_animal_list )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onExit, id = self.m_menuItem_exit.GetId() )
        self.Bind( wx.EVT_MENU, self.onNext, id = self.m_menuItem_next.GetId() )
        self.Bind( wx.EVT_MENU, self.onPrev, id = self.m_menuItem_prev.GetId() )
        self.m_panel.Bind( wx.EVT_PAINT, self.onPaint )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onExit( self, event ):
        event.Skip()

    def onNext( self, event ):
        event.Skip()

    def onPrev( self, event ):
        event.Skip()

    def onPaint( self, event ):
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

        gbSizer1.Add( self.m_name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"価値"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText5, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_gauge_value = wx.Gauge( self.m_panel_page1, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.GA_HORIZONTAL )
        self.m_gauge_value.SetValue( 0 )
        self.m_gauge_value.SetBackgroundColour( wx.Colour( 128, 255, 0 ) )

        gbSizer1.Add( self.m_gauge_value, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"権利"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText7, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_gauge_right = wx.Gauge( self.m_panel_page1, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.GA_HORIZONTAL )
        self.m_gauge_right.SetValue( 0 )
        self.m_gauge_right.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_gauge_right.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        gbSizer1.Add( self.m_gauge_right, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_class_name = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_class_name.Wrap( -1 )

        self.m_class_name.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_class_name, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


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

        self.m_slider_value = wx.Slider( self.m_panel_page2, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL|wx.SL_SELRANGE )
        self.m_slider_value.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_slider_value.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
        self.m_slider_value.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_slider_value.SetMinSize( wx.Size( -1,10 ) )

        gbSizer2.Add( self.m_slider_value, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel_page2, wx.ID_ANY, _(u"権利初期値"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText9, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_slider_right = wx.Slider( self.m_panel_page2, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL|wx.SL_SELRANGE )
        self.m_slider_right.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_slider_right.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        self.m_slider_right.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_slider_right.SetMinSize( wx.Size( -1,10 ) )

        gbSizer2.Add( self.m_slider_right, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel_page2, wx.ID_ANY, _(u"２ページ目"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        self.m_staticText10.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText_name = wx.StaticText( self.m_panel_page2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_name.Wrap( -1 )

        self.m_staticText_name.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText_name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl_value = wx.TextCtrl( self.m_panel_page2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,12 ), wx.TE_PROCESS_ENTER )
        self.m_textCtrl_value.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_textCtrl_value.SetMinSize( wx.Size( 25,12 ) )

        gbSizer2.Add( self.m_textCtrl_value, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl_right = wx.TextCtrl( self.m_panel_page2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,12 ), wx.TE_PROCESS_ENTER )
        self.m_textCtrl_right.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_textCtrl_right.SetMinSize( wx.Size( 25,12 ) )

        gbSizer2.Add( self.m_textCtrl_right, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.m_panel_page2.SetSizer( gbSizer2 )
        self.m_panel_page2.Layout()
        gbSizer2.Fit( self.m_panel_page2 )
        self.m_simplebook.AddPage( self.m_panel_page2, _(u"a page"), False )

        bSizer6.Add( self.m_simplebook, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        # Connect Events
        self.Bind( wx.EVT_LEFT_DCLICK, self.onAnimalClick )
        self.m_name.Bind( wx.EVT_TEXT, self.onAnimalNameChange )
        self.m_name.Bind( wx.EVT_TEXT_ENTER, self.onAnimalNameChange )
        self.m_slider_value.Bind( wx.EVT_SLIDER, self.onValueChanged )
        self.m_slider_right.Bind( wx.EVT_SLIDER, self.onRightChanged )
        self.m_textCtrl_value.Bind( wx.EVT_TEXT_ENTER, self.onValueText )
        self.m_textCtrl_right.Bind( wx.EVT_TEXT_ENTER, self.onRightText )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onAnimalClick( self, event ):
        event.Skip()

    def onAnimalNameChange( self, event ):
        event.Skip()


    def onValueChanged( self, event ):
        event.Skip()

    def onRightChanged( self, event ):
        event.Skip()

    def onValueText( self, event ):
        event.Skip()

    def onRightText( self, event ):
        event.Skip()


