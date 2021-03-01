import random


class Market:
    def __init__(self, animal_list, log):
        self.animal_list = animal_list
        self.log = log

    def trade(self):
        for animal_buyer in self.animal_list:
            price = animal_buyer.buy()
            if price is None:
                self.log("【{0}】は権利不足でした".format(animal_buyer.get_name()))
                continue
            seller_list = [animal for animal in self.animal_list if animal.request(price)]
            length = len(seller_list)
            if length == 0:
                self.log("【{0}】は購入できませんでした".format(animal_buyer.get_name()))
                continue
            select = random.randint(0, length - 1)
            seller_list[select].sell(price)
            animal_buyer.settlement(price)
            self.log(
                "【{0}】は【{1}】から{2}で購入しました".format(animal_buyer.get_name(), seller_list[select].get_name(), price))

        for animal in self.animal_list:
            animal.production()         # 生産
            animal.consume()            # 消費