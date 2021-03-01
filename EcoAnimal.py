import wx
from Animal import AnimalModel, AnimalParameterSettingDialog, AnimalView
from Market import Market
import pandas as pd
from SimpleBookSample import MainFrame


# https://note.nkmk.me/python-pandas-assign-append/

class EcoAnimal:
    def __init__(self):
        self.animal_list = pd.DataFrame()
        for i in range(1, 109):
            animal_name = "Animal{0}".format(str(i))
            df = pd.DataFrame({
                'object': [None],
                'name': [animal_name],  # アニマル名
                'initial_right': [50],  # 権利の初期値
                'create_value': [30],  # 価値の生産量
                'value': [30],  # 価値の量
                'right': [50],  # 権利の量
                'consumption': [30],  # 消費量
                'purchase_amount': [30],  # 購入量
            })
            animal = AnimalModel(df)
            df['object'] = animal
            self.animal_list = self.animal_list.append(df, ignore_index=True)

        self.view = EcoAnimalView(None, self)
        self.view.Show()

    def get_animal_list(self):
        return self.animal_list['object'].values.tolist()

    def reset(self):
        for animal in self.animal_list['object']:
            animal.reset()

        return self.animal_list

    def trade(self):
        market = Market(self.get_animal_list(), self.view.logout)
        market.trade()
        self.view.update_animals()




class EcoAnimalView(MainFrame):
    def __init__(self, parent, model):
        super().__init__(parent)

        self.model = model
        animal_model_list = self.model.get_animal_list()
        self.bSizer_animal_list = wx.BoxSizer(wx.VERTICAL)

        self.animal_list = []
        for i in range(108):
            animal = AnimalView(self.m_scrolledWindow, animal_model_list[i], wx.ID_ANY, wx.DefaultPosition,
                                wx.DefaultSize, 0)
            self.bSizer_animal_list.Add(animal, 1, wx.EXPAND | wx.ALL, 5)
            self.animal_list.append(animal)
            animal.set_root_window(self)

        self.m_scrolledWindow.SetSizer(self.bSizer_animal_list)

    def logout(self, text):
        self.m_textCtrl.AppendText(text + '\n')

    def onPaint(self, event):
        for i in range(9):
            for j in range(12):
                x = j * 70 + 30
                y = i * 40 + 20
                animal = self.animal_list[i * 12 + j]
                animal.paint(self.m_panel, x, y)

    def onExit(self, event):
        self.Destroy()

    def onNext(self, event):
        self.next_page()

    def onPrev(self, event):
        self.prev_page()

    def next_page(self):
        for panel in self.animal_list:
            book = panel.m_simplebook
            last_page = book.GetPageCount()
            current_page = book.GetSelection()
            if current_page < last_page:
                book.ChangeSelection(current_page + 1)

    def prev_page(self):
        for panel in self.animal_list:
            book = panel.m_simplebook
            current_page = book.GetSelection()
            if current_page > 0:
                book.ChangeSelection(current_page - 1)

    def onTrade(self, event):
        self.model.trade()

    def onReset(self, event):
        self.model.reset()
        self.Refresh()

    def update_animals(self):
        for animal in self.animal_list:
            animal.set_control()
        self.Refresh()

    def onTradeRun(self, event):
        self.m_timer.Start(500)

    def onTradeStop(self, event):
        self.m_timer.Stop()

    def onTimer(self, event):
        self.model.trade()

    def onParameterSetting(self, event):
        dialog = AnimalParameterSettingDialog(self)
        result = dialog.ShowModal()
        if result != wx.ID_OK:
            return

        for animal in self.animal_list:
            animal.set_parameter(dialog)


if __name__ == "__main__":
    app = wx.App()
    obj = EcoAnimal()
    app.MainLoop()
