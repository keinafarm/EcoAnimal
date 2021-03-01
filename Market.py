##################################################
#
#   取引処理
#
##################################################

class Market:
    def __init__(self, animal_list, log):
        """
        取引処理クラス
        :param animal_list: ModelのAnimalリスト
        :param log: Viewのlog表示
        """
        self.animal_list = animal_list              # ModelのAnimalリスト
        self.log = log                              # Viewのlog表示

    def trade(self):
        """
        取引をする
        :return:
        """
        for animal in self.animal_list:
            animal.production()  # 生産

        for animal_buyer in self.animal_list:
            animal_buyer.buy(self.animal_list, self.log)    # 取引

        for animal in self.animal_list:
            animal.consume()  # 消費
