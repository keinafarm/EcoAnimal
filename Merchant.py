############################################################
#
#   商人：自らは生産しないが、購入したものに利益を載せて販売する人
#
############################################################

from DataBase import DataBase
from Animal import AnimalModel, AnimalParameterSettingDialog, AnimalView


#############
#
#   全体のデータ管理オブジェクト
#
#############
class MerchantData(DataBase):
    def __init__(self):
        super().__init__()
        self.property_name_list.append('margin')
        self.initial_values['margin'] = 0

    def load_property(self, obj):
        super().load_property(obj)
        obj.margin = self.initial_values['margin']

    def store_property(self, obj):
        super().store_property(obj)
        self.initial_values['margin'] = obj.margin

    #############
    #   プロパティ Getter,setter
    #############
    #
    #   Getter
    #
    def get_margin(self, index):
        return self.animal_properties.at[index, 'margin']

    def set_margin(self, index, amount):
        self.animal_properties.at[index, 'margin'] = amount


#############
#
#   個別のデータ管理オブジェクト(Model)
#
#############
class MerchantModel(AnimalModel):
    def __init__(self, index, name):
        super().__init__(index, name)
        self.margin = 0

    def set_parameter(self, source):
        super().set_parameter(source)
        self.margin = source.margin

    def price(self, amount):
        """
        購入量を提示して、価格を得る
        :param amount: 購入量
        :return:[このオブジェクト,販売価格]
        """
        return [self, amount * (1 + self.margin / 100)]  # 価格はマージンを載せる
