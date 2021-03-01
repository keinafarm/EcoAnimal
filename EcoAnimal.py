import wx
from Gui import Gui
from Animal import AnimalModel
from Market import Market
import pandas as pd


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

        self.view = Gui(None, self)
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


if __name__ == "__main__":
    app = wx.App()
    obj = EcoAnimal()
    app.MainLoop()
