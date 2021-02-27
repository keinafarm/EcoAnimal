import wx
from Gui import Gui
from AnimalBook import  AnimalBookModel

class EcoAnimal():
    def __init__(self):
        self.animal_list = []
        for i in range(1,101):
            animal_name = "Animal{0}".format(str(i))
            animal = AnimalBookModel( animal_name )
            self.animal_list.append(animal)

        self.view = Gui(None, self)

        self.view.Show()

    def get_animal_list(self):
        return self.animal_list

    def reset(self):
        for animal in self.animal_list:
            animal.reset()

        return self.animal_list

if __name__ == "__main__":
    app = wx.App()
    obj = EcoAnimal()
    app.MainLoop()
