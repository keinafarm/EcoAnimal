############################################################
#
#   商人：自らは生産しないが、購入したものに利益を載せて販売する人
#
############################################################

from Animal import AnimalModel

class MerchantModel(AnimalModel):
    @classmethod
    def migration(cls):
        AnimalModel.property_name_list.append( 'margin' )
        AnimalModel.initial_values['margin'] = 0

    def __init__(self, index, name):
        super().__init__(index, name)
        self.margin =

