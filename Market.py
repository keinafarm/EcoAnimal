import random


class Market:
    def __init__(self, animal_list, log):
        self.animal_list = animal_list
        self.log = log

    def trade(self):
        for animal_buyer in self.animal_list:
            price = animal_buyer.buy()
            seller_list = [animal for animal in self.animal_list if animal.request(price)]
            length = len(seller_list)
            if length == 0:
                self.log.out("【{0}】は購入できませんでした".format(animal_buyer.get_name()))
                continue
            select = random.randint(0, length - 1)
            seller_list[select].sell(price)
            self.log.out(
                "【{0}】は【{1}】から{2}で購入しました".format(animal_buyer.get_name(), seller_list[select].get_name(), price))
