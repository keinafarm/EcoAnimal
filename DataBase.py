############################################################
#
#   全データを管理するクラス
#
############################################################
import pandas as pd


class DataBase:
    singleton = None

    @classmethod
    def create(cls, class_constructor):
        if cls.singleton is None:
            cls.singleton = class_constructor()

    @classmethod
    def obj(cls):
        return cls.singleton

    def __init__(self):
        self.animal_properties = None
        self.property_name_list = ['object', 'name', 'value', 'right', 'create_value', 'initial_right', 'consumption',
                                   'purchase_amount']
        self.initial_values = {'object': None, 'name': None, 'right': 50, 'value': 20, 'create_value': 20,
                               'initial_right': 50, 'consumption': 20, 'purchase_amount': 20}
        self.animal_count = 0

    def initialize(self, animals):
        self.animal_properties = pd.DataFrame([self.initial_values] * animals, columns=self.property_name_list)
        self.animal_count = animals

    def set_initial_values(self, initial_value):
        """
        全体の初期値を設定する
        :param initial_value: 初期値リスト（辞書型）
        :return:
        """
        self.initial_values = initial_value

    def load_property(self, obj):
        obj.initial_right = self.initial_values['initial_right']
        obj.create_value = self.initial_values['create_value']
        obj.consumption = self.initial_values['consumption']
        obj.purchase_amount = self.initial_values['purchase_amount']

    def store_property(self, obj):
        self.initial_values['initial_right'] = obj.initial_right
        self.initial_values['create_value'] = obj.create_value
        self.initial_values['consumption'] = obj.consumption
        self.initial_values['purchase_amount'] = obj.purchase_amount

    def save(self, pathname):
        save_list = self.animal_properties.copy()
        save_list['object'] = None
        save_list.to_excel(pathname)

    def load(self, pathname):
        animal_list = pd.read_excel(pathname)
        if len(animal_list) != self.animal_count:
            return "データ数は{0}です。(現在:{1})".format(self.animal_count, len(animal_list))

        self.animal_properties = animal_list
        return None

    #############
    #   プロパティ Getter,setter
    #############
    #
    #   Getter
    #
    @property
    def df(self):
        return self.animal_properties

    def get_name(self, index):
        return self.animal_properties.at[index, 'name']

    def get_initial_right(self, index):
        return self.animal_properties.at[index, 'initial_right']

    def get_create_value(self, index):
        return self.animal_properties.at[index, 'create_value']

    def get_value(self, index):
        return self.animal_properties.at[index, 'value']

    def get_right(self, index):
        return self.animal_properties.at[index, 'right']

    def get_consumption(self, index):
        return self.animal_properties.at[index, 'consumption']

    def get_purchase_amount(self, index):
        return self.animal_properties.at[index, 'purchase_amount']

    #
    #   Setter
    #
    def set_name(self, index, text):
        self.animal_properties.at[index, 'name'] = text

    def set_initial_right(self, index, amount):
        self.animal_properties.at[index, 'initial_right'] = amount

    def set_create_value(self, index, amount):
        self.animal_properties.at[index, 'create_value'] = amount

    def set_value(self, index, amount):
        self.animal_properties.at[index, 'value'] = amount

    def set_right(self, index, amount):
        self.animal_properties.at[index, 'right'] = amount

    def set_consumption(self, index, amount):
        self.animal_properties.at[index, 'consumption'] = amount

    def set_purchase_amount(self, index, amount):
        self.animal_properties.at[index, 'purchase_amount'] = amount

    def set_object(self, index, obj):
        self.animal_properties.at[index, 'object'] = obj
