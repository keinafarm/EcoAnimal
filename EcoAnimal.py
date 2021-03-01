import wx
from Gui import Gui
from Animal import AnimalModel
from Market import Market


class EcoAnimal:
    def __init__(self):
        self.animal_list = []
        for i in range(1, 109):
            animal_name = "Animal{0}".format(str(i))
            animal = AnimalModel(animal_name)
            self.animal_list.append(animal)

        self.view = Gui(None, self)

        self.view.Show()

    def get_animal_list(self):
        return self.animal_list

    def reset(self):
        for animal in self.animal_list:
            animal.reset()

        return self.animal_list

    def trade(self):
        market = Market(self.animal_list, self.view.logout)
        market.trade()
        self.view.update_animals()

if __name__ == "__main__":
    app = wx.App()
    obj = EcoAnimal()
    app.MainLoop()
