

class Market:
    def __init__(self, animal_list, log):
        self.animal_list = animal_list
        self.log = log

    def trade(self):
        for animal in self.animal_list:
            animal.production()  # 生産

        for animal_buyer in self.animal_list:
            animal_buyer.buy(self.animal_list, self.log)

        for animal in self.animal_list:
            animal.consume()  # 消費
