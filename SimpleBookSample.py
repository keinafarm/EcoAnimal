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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 915,698 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.m_menubar = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menuItem2 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"MyMenuItem"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menuItem2 )

        self.m_menubar.Append( self.m_menu_file, _(u"File") )

        self.m_menu_BookList = wx.Menu()
        self.m_menubar.Append( self.m_menu_BookList, _(u"Book List") )

        self.SetMenuBar( self.m_menubar )

        self.bSizer_animal_list = wx.GridBagSizer( 0, 0 )
        self.bSizer_animal_list.SetFlexibleDirection( wx.BOTH )
        self.bSizer_animal_list.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel.SetMinSize( wx.Size( 600,400 ) )

        self.bSizer_animal_list.Add( self.m_panel, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

        self.m_scrolledWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 280,-1 ), wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow.SetScrollRate( 5, 5 )
        self.m_scrolledWindow.SetMinSize( wx.Size( 280,400 ) )

        self.bSizer_animal_list.Add( self.m_scrolledWindow, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

        self.m_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl.SetMinSize( wx.Size( 890,200 ) )

        self.bSizer_animal_list.Add( self.m_textCtrl, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )


        self.SetSizer( self.bSizer_animal_list )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class SimpleBookPanel
###########################################################################

class SimpleBookPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 260,90 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetMinSize( wx.Size( 260,90 ) )
        self.SetMaxSize( wx.Size( 271,103 ) )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_simplebook1 = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_panel_page1 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText4 = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"名前"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_name = wx.TextCtrl( self.m_panel_page1, wx.ID_ANY, _(u"１ページ目"), wx.DefaultPosition, wx.Size( -1,15 ), 0 )
        self.m_name.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"価値"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText5, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_gauge1 = wx.Gauge( self.m_panel_page1, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 )
        gbSizer1.Add( self.m_gauge1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"権利"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText7, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_gauge2 = wx.Gauge( self.m_panel_page1, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.GA_HORIZONTAL )
        self.m_gauge2.SetValue( 0 )
        gbSizer1.Add( self.m_gauge2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_class_name = wx.StaticText( self.m_panel_page1, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_class_name.Wrap( -1 )

        self.m_class_name.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_class_name, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.m_panel_page1.SetSizer( gbSizer1 )
        self.m_panel_page1.Layout()
        gbSizer1.Fit( self.m_panel_page1 )
        self.m_simplebook1.AddPage( self.m_panel_page1, _(u"a page"), False )
        self.m_panel_page2 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText8 = wx.StaticText( self.m_panel_page2, wx.ID_ANY, _(u"項目１"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText8, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_slider1 = wx.Slider( self.m_panel_page2, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL )
        gbSizer2.Add( self.m_slider1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel_page2, wx.ID_ANY, _(u"項目２"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText9, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_slider2 = wx.Slider( self.m_panel_page2, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,10 ), wx.SL_HORIZONTAL )
        gbSizer2.Add( self.m_slider2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel_page2, wx.ID_ANY, _(u"２ページ目"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        self.m_staticText10.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gbSizer2.Add( self.m_staticText10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.m_panel_page2.SetSizer( gbSizer2 )
        self.m_panel_page2.Layout()
        gbSizer2.Fit( self.m_panel_page2 )
        self.m_simplebook1.AddPage( self.m_panel_page2, _(u"a page"), False )

        bSizer6.Add( self.m_simplebook1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

    def __del__( self ):
        pass


