# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frame_window
###########################################################################

class Frame_window ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"新添雨跟打器", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer24.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        fgSizer1 = wx.FlexGridSizer( 6, 1, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        状态栏 = wx.BoxSizer( wx.VERTICAL )

        状态栏.SetMinSize( wx.Size( -1,20 ) )
        成绩 = wx.BoxSizer( wx.HORIZONTAL )

        成绩.SetMinSize( wx.Size( 800,-1 ) )
        self.m_button历史 = wx.Button( self, wx.ID_ANY, u"0000", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_button历史.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_button历史.SetBackgroundColour( wx.Colour( 106, 92, 97 ) )
        self.m_button历史.SetMinSize( wx.Size( 55,-1 ) )

        成绩.Add( self.m_button历史, 0, 0, 5 )

        self.m_button成绩1 = wx.Button( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_button成绩1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_button成绩1.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )
        self.m_button成绩1.SetMinSize( wx.Size( 115,-1 ) )

        成绩.Add( self.m_button成绩1, 0, 0, 5 )

        self.m_button成绩2 = wx.Button( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_button成绩2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_button成绩2.SetBackgroundColour( wx.Colour( 77, 83, 91 ) )
        self.m_button成绩2.SetMinSize( wx.Size( 115,-1 ) )

        成绩.Add( self.m_button成绩2, 0, 0, 5 )

        self.m_button成绩3 = wx.Button( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_button成绩3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_button成绩3.SetBackgroundColour( wx.Colour( 88, 93, 100 ) )
        self.m_button成绩3.SetMinSize( wx.Size( 115,-1 ) )

        成绩.Add( self.m_button成绩3, 0, 0, 5 )

        self.m_button今日1 = wx.Button( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_button今日1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_button今日1.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )
        self.m_button今日1.SetMinSize( wx.Size( 115,-1 ) )

        成绩.Add( self.m_button今日1, 0, 0, 5 )

        self.m_button今日2 = wx.Button( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_button今日2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_button今日2.SetBackgroundColour( wx.Colour( 77, 83, 91 ) )
        self.m_button今日2.SetMinSize( wx.Size( 115,-1 ) )

        成绩.Add( self.m_button今日2, 0, 0, 5 )

        self.m_button今日3 = wx.Button( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_button今日3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_button今日3.SetBackgroundColour( wx.Colour( 88, 93, 100 ) )
        self.m_button今日3.SetMinSize( wx.Size( 115,-1 ) )

        成绩.Add( self.m_button今日3, 0, 0, 5 )

        self.m_button菜单 = wx.Button( self, wx.ID_ANY, u"菜单", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_button菜单.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.m_button菜单.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_button菜单.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )
        self.m_button菜单.SetMinSize( wx.Size( 50,-1 ) )

        成绩.Add( self.m_button菜单, 0, 0, 5 )


        状态栏.Add( 成绩, 0, 0, 5 )

        信息 = wx.BoxSizer( wx.HORIZONTAL )

        信息.SetMinSize( wx.Size( -1,20 ) )
        self.文段 = wx.Button( self, wx.ID_ANY, u"无文段", wx.DefaultPosition, wx.Size( 60,20 ), wx.BORDER_NONE )
        self.文段.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.文段.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.文段.SetBackgroundColour( wx.Colour( 174, 86, 89 ) )

        信息.Add( self.文段, 0, 0, 5 )

        self.收藏 = wx.Button( self, wx.ID_ANY, u"★", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.收藏.SetForegroundColour( wx.Colour( 58, 63, 71 ) )
        self.收藏.SetBackgroundColour( wx.Colour( 89, 95, 104 ) )

        信息.Add( self.收藏, 0, 0, 5 )

        self.标题 = wx.Button( self, wx.ID_ANY, u"无标题", wx.DefaultPosition, wx.Size( 500,20 ), wx.BORDER_NONE )
        self.标题.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.标题.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.标题.SetBackgroundColour( wx.Colour( 52, 136, 136 ) )

        信息.Add( self.标题, 0, 0, 5 )

        self.汇总 = wx.Button( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.汇总.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.汇总.SetBackgroundColour( wx.Colour( 89, 95, 104 ) )

        信息.Add( self.汇总, 0, 0, 5 )

        self.文章 = wx.Button( self, wx.ID_ANY, u"文章", wx.DefaultPosition, wx.Size( 70,20 ), wx.BORDER_NONE )
        self.文章.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.文章.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.文章.SetBackgroundColour( wx.Colour( 123, 121, 123 ) )

        信息.Add( self.文章, 0, 0, 5 )

        self.字数 = wx.Button( self, wx.ID_ANY, u"共124字", wx.Point( -1,-1 ), wx.Size( 60,20 ), wx.BORDER_NONE )
        self.字数.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.字数.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.字数.SetBackgroundColour( wx.Colour( 174, 118, 66 ) )

        信息.Add( self.字数, 0, 0, 5 )

        self.群设置 = wx.Button( self, wx.ID_ANY, u"未设置", wx.DefaultPosition, wx.Size( 60,20 ), wx.BORDER_NONE )
        self.群设置.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.群设置.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.群设置.SetBackgroundColour( wx.Colour( 13, 114, 17 ) )

        信息.Add( self.群设置, 0, 0, 5 )


        状态栏.Add( 信息, 0, 0, 5 )

        进度 = wx.BoxSizer( wx.VERTICAL )

        进度.SetMinSize( wx.Size( -1,20 ) )
        self.m_gauge3 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 800,20 ), wx.GA_HORIZONTAL )
        self.m_gauge3.SetValue( 0 )
        self.m_gauge3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_gauge3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_gauge3.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        进度.Add( self.m_gauge3, 0, 0, 5 )


        状态栏.Add( 进度, 1, 0, 5 )


        fgSizer1.Add( 状态栏, 1, wx.EXPAND, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"欢迎使用添雨跟打器极致版。快捷键列表：F1暂停、F2成绩汇总、F3重打、F4载文，ALT+E从剪切板载文、F5换群、F6发送下一段文章（新）、F7分享发文、F8发送上次成绩。如您有什么建议，请到http://www.taliove.com回复留言。", wx.Point( -1,-1 ), wx.Size( 800,330 ), wx.TE_MULTILINE|wx.TE_READONLY )
        self.m_textCtrl4.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.m_textCtrl4.SetBackgroundColour( wx.Colour( 228, 228, 228 ) )

        fgSizer1.Add( self.m_textCtrl4, 1, wx.EXPAND, 5 )

        self.bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.bSizer4.SetMinSize( wx.Size( -1,20 ) )
        self.m_buttonS = wx.Button( self, wx.ID_ANY, u"S", wx.Point( -1,-1 ), wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_buttonS.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_buttonS.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_buttonS, 0, 0, 5 )

        self.m_buttonR = wx.Button( self, wx.ID_ANY, u"R", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_buttonR.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_buttonR.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_buttonR, 0, 0, 5 )

        self.m_buttonP = wx.Button( self, wx.ID_ANY, u"P", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_buttonP.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_buttonP.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_buttonP, 0, 0, 5 )

        self.m_buttonL = wx.Button( self, wx.ID_ANY, u"L", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_buttonL.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_buttonL.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_buttonL, 0, 0, 5 )

        self.m_buttonC = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_buttonC.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_buttonC.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_buttonC, 0, 0, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_button3.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_button3.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_button3, 0, 0, 5 )

        self.m_button4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_button4.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_button4.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_button4, 0, 0, 5 )

        self.m_button5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_button5.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_button5.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_button5, 0, 0, 5 )

        self.m_buttonI = wx.Button( self, wx.ID_ANY, u"I", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_buttonI.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_buttonI.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_buttonI, 0, 0, 5 )

        self.m_buttonT = wx.Button( self, wx.ID_ANY, u"T", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE )
        self.m_buttonT.SetForegroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_buttonT.SetBackgroundColour( wx.Colour( 60, 67, 77 ) )

        self.bSizer4.Add( self.m_buttonT, 0, 0, 5 )


        self.bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText跟打记录 = wx.StaticText( self, wx.ID_ANY, u"今0/总1035/连0/共3天", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        self.m_staticText跟打记录.Wrap( -1 )

        self.m_staticText跟打记录.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.m_staticText跟打记录.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_staticText跟打记录.SetBackgroundColour( wx.Colour( 30, 129, 103 ) )

        self.bSizer4.Add( self.m_staticText跟打记录, 0, 0, 5 )


        fgSizer1.Add( self.bSizer4, 1, wx.EXPAND, 5 )

        self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, u"我我我我", wx.DefaultPosition, wx.Size( 800,180 ), wx.TE_MULTILINE )
        self.m_textCtrl41.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.m_textCtrl41.SetBackgroundColour( wx.Colour( 228, 228, 228 ) )

        fgSizer1.Add( self.m_textCtrl41, 1, wx.EXPAND, 5 )


        bSizer24.Add( fgSizer1, 1, wx.EXPAND, 5 )


        bSizer24.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer24 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SIZE, self.on_size )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_size( self, event ):
        event.Skip()


