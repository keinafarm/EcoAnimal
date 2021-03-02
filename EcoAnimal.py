########################################################################
#
#   シンプルな経済モデルで遊んで見るアプリ
#   アニマルが活動する様子を眺める
#
#   https://note.nkmk.me/python-pandas-assign-append/
#
########################################################################

import wx
from Animal import AnimalModel, AnimalParameterSettingDialog, AnimalView
from Market import Market
import pandas as pd
from SimpleBookSample import MainFrame
import openpyxl

ANIMALS = 108  # アニマルの数（色んな数で割りやすいから２と3の倍数にした）


class AnimalParameter:
    df = pd.DataFrame({  # アニマルのプロパティの初期値
        'object': [None],
        'name': [None],  # アニマル名
        'initial_right': [50],  # 権利の初期値
        'create_value': [30],  # 価値の生産量
        'value': [0],  # 価値の量
        'right': [50],  # 権利の量
        'consumption': [30],  # 消費量
        'purchase_amount': [30],  # 購入量
    })

    @classmethod
    def get_property(cls):
        """
        保存してある初期値データを提供する
        :return:
        """
        return cls.df.copy()

    @classmethod
    def store_property(cls, target):
        """
        初期値データを保存する
        :param target: 新たな初期値が格納されているオブジェクト
        :return:
        """
        cls.df.at[0,'initial_right'] = target.initial_right
        cls.df.at[0,'create_value'] = target.create_value
        cls.df.at[0,'consumption'] = target.consumption
        cls.df.at[0,'purchase_amount'] = target.purchase_amount

    @classmethod
    def load_property(cls, target):
        target.initial_right = cls.df.at[0, 'initial_right']
        target.create_value = cls.df.at[0, 'create_value']
        target.consumption = cls.df.at[0, 'consumption']
        target.purchase_amount = cls.df.at[0, 'purchase_amount']


class EcoAnimal:
    def __init__(self):
        """
            アプリのメインクラス
            全アニマルのデータをPandasのDataFrameで管理している
        """
        self._animal_list = pd.DataFrame()  # アニマルリストを初期化
        for i in range(ANIMALS):
            # 初期値
            animal_name = "Animal{0}".format(i + 1)  # アニマル名の初期値
            df = AnimalParameter.get_property()  # アニマルプロパティの初期値
            df.at[0,"name"] = animal_name
            animal = AnimalModel(df)  # アニマルを生成
            df.at[0,'object'] = animal  # インスタンスを保存
            self._animal_list = self._animal_list.append(df, ignore_index=True)  # リストに登録

        self.view = EcoAnimalView(None, self)  # viewを作成
        self.view.Show()  # 表示

    @property
    def animal_list(self):
        """
        リスト形式でアニマルリストを提供する
        :return:
        """
        df = self._animal_list.loc[:,'object']
        ret_list = df.values.tolist()
        return ret_list

    def reset(self):
        """
        全アニマルの価値と権利を初期値に戻す
        :return:
        """
        for animal in self.animal_list:
            animal.reset()
        self.view.update_animals()  # 表示を更新

    def trade(self):
        """
        全アニマルに対して取引を行う
        :return:
        """
        market = Market(self.animal_list, self.view.log)  # 市場オブジェクトを生成
        market.trade()  # 市場オブジェクトに取引をさせる
        self.view.update_animals()  # 表示を更新

    def save(self, pathname):
        """
        ファイルにアニマルデータを書き込む
        https://note.nkmk.me/python-pandas-to-pickle-read-pickle/
        https://note.nkmk.me/python-pandas-to-excel/
        :param pathname: 出力先ファイル
        :return: 
        """
        save_list = self._animal_list.copy()
        save_list.loc[:,'object'] = None          # オブジェクトはクリアしておく
        save_list.to_excel(pathname, index=False)

    def load(self, pathname):
        """
        https://note.nkmk.me/python-pandas-dataframe-for-iteration/
        df.loc[x:y]['colomn'] = は スライスで作成されたコピーに代入している
        df.loc[x:y,'colomn'] = は スライスで指定した場所に直接代入している

        df.reset_index(drop=True, inplace=True)
        取り出したData Frameのindexを0にする
        https://note.nkmk.me/python-pandas-reset-index/
        :param pathname:
        :return:
        """
        animal_list = pd.read_excel(pathname, index_col=None)
        if len(animal_list) != ANIMALS:
            self.view.m_statusBar.SetStatusText("データ数は{0}です。(現在:{1})".format(ANIMALS, len(animal_list)))  # あとでdialog化
            return

        self._animal_list = pd.DataFrame()  # アニマルリストを初期化
        for i in range(ANIMALS):
            df = animal_list.loc[i:i].copy(deep=False)                  # DataFrame型で取得しようと思ったら範囲していしないといけない
                                                                        # deep=Falseでないと、参照になる
            df.reset_index(drop=True, inplace=True)                     # indexをクリアしておかないと、AnimalModelが代入する時困る
            animal = AnimalModel(df)
            df['object'] = animal
            self._animal_list = self._animal_list.append(df, ignore_index=True)  # リストに登録

        self.view.restructure(self.animal_list)                         # 読み直したデータで画面を再構築する


class EcoAnimalView(MainFrame):
    def __init__(self, parent, model):
        """
        全体的な表示画面とGUIの操作
        :param parent: 親のウィンドウ（普通はNone)
        :param model: このViewに対するモデル
        """
        super().__init__(parent)

        self.model = model  # モデルを保持
        self.bSizer_animal_list = wx.BoxSizer(wx.VERTICAL)  # アニマル設定パネル（右側）のレイアウト

        self.animal_list = []
        for i in range(ANIMALS):
            animal = AnimalView(self.m_scrolledWindow, self.model.animal_list[i], wx.ID_ANY, wx.DefaultPosition,
                                wx.DefaultSize, 0)
            self.bSizer_animal_list.Add(animal, 1, wx.EXPAND | wx.ALL, 5)
            self.animal_list.append(animal)  # アニマルのViewを作って登録
            animal.set_root_window(self)  # 各アニマルに、このビューを通知(アニマルのparentはm_scrolledWindowなので、何かと不便)

        self.m_scrolledWindow.SetSizer(self.bSizer_animal_list)

    def restructure(self, animal_list):
        for i in range(len(animal_list)):
            model = animal_list[i]
            self.animal_list[i].set_model(model)
        self.Refresh()

    def log(self, text):
        """
        ログ(下のテキストエリア）を出力する
        :param text:出力するログ
        :return:
        """
        self.m_textCtrl.AppendText(text + '\n')

    def update_animals(self):
        """
        表示を最新情報で更新する
        :return:
        """
        for animal in self.animal_list:
            animal.set_control()
        self.Refresh()

    def onPaint(self, event):
        """
        左のアイコン欄の描画
        :param event:
        :return:
        """
        i = 0
        j = 0
        for animal in self.animal_list:
            x = j * 70 + 30  # animal_listの分だけ、横12列ずつ配置する
            y = i * 40 + 20
            animal.paint(self.m_panel, x, y)
            j += 1
            if j > 12:
                i += 1
                j = 0

    ##########################
    #   メニュー処理
    ##########################
    def onSave(self, event):
        """
        [ファイル]-[保存]メニュー
        https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html
        :param event:
        :return:
        """
        with wx.FileDialog(self, "アニマルデータを保存", wildcard="CSV files (*.xlsx)|*.xlsx",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            try:
                self.model.save(pathname)
            except IOError:
                self.m_statusBar.SetStatusText("{0}に書き込めませんでした".format(pathname))
                return

        self.m_statusBar.SetStatusText("{0}に保存しました".format(pathname))

    def onLoad(self, event):
        """
        [ファイル]-[読み出し]メニュー
        :param event:
        :return:
        """
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "アニマルデータを読み出し", wildcard="CSV files (*.xlsx)|*.xlsx",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                self.model.load(pathname)
            except IOError:
                self.m_statusBar.SetStatusText("{0}から読み込めませんでした".format(pathname))
                return

        self.onReset()
        self.m_statusBar.SetStatusText("{0}から読み出しました".format(pathname))

    def onLogSave(self, event):
        """
        [ファイル]-[ログ保存]メニュー
        :param event:
        :return:
        """
        event.Skip()

    def onExit(self, event):
        """
        [ファイル]-[終了]メニュー
        :param event:
        :return:
        """
        self.Destroy()

    def onTrade(self, event):
        """
        [実行]-[取引]メニュー
        モデルに取引を通知
        :param event:
        :return:
        """
        self.model.trade()

    def onTradeRun(self, event):
        """
        [実行]-[連続取引開始]メニュー
        :param event:
        :return:
        """
        self.m_timer.Start(500)  # 0.5secのタイマーをかける

    def onTradeStop(self, event):
        """
        [実行]-[連続取引停止]メニュー
        :param event:
        :return:
        """
        self.m_timer.Stop()  # タイマーを停止

    def onTimer(self, event):
        """
        タイムアウトのたびに、取引
        :param event:
        :return:
        """
        self.model.trade()

    def onNext(self, event):
        """
        [アニマル]-[次へ]メニュー
        :param event:
        :return:
        """
        self.next_page()

    def onPrev(self, event):
        """
        [アニマル]-[前へ]メニュー
        アニマル設定Bookのページをめくる
        :param event:
        :return:
        """
        self.prev_page()

    def next_page(self):
        """
        アニマル設定Bookのページをめくる
        :return:
        """
        for panel in self.animal_list:  # 全アニマルのviewに対して
            book = panel.m_simplebook  # Bookの
            last_page = book.GetPageCount()  # ページ数と
            current_page = book.GetSelection()  # 現在のページを取得して
            if current_page < last_page:  # 最後まで行ってなかったら
                book.ChangeSelection(current_page + 1)  # ページをめくる

    def prev_page(self):
        """
        アニマル設定Bookのページをめくる
        :return:
        """
        for panel in self.animal_list:  # 全アニマルのviewに対して
            book = panel.m_simplebook  # Bookの
            current_page = book.GetSelection()  # 現在のページを取得して
            if current_page > 0:  # 先頭でなかったら
                book.ChangeSelection(current_page - 1)  # ページをめくる

    def onParameterSetting(self, event):
        """
        [アニマル]-[一括設定]メニュー
        :param event:
        :return:
        """
        dialog = AnimalParameterSettingDialog(self, AnimalParameter.load_property)
        result = dialog.ShowModal()
        if result != wx.ID_OK:
            return
        AnimalParameter.store_property(dialog)
        for animal in self.animal_list:
            animal.set_parameter(dialog)

    def onReset(self, event):
        """
        [アニマル]-[初期値に戻す]メニュー
        :param event:
        :return:
        """
        self.model.reset()
        self.Refresh()


if __name__ == "__main__":
    app = wx.App()
    obj = EcoAnimal()
    app.MainLoop()
