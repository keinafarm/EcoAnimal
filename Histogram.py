import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

############################################################
#
#   ヒストグラムを表示する
#   https://qiita.com/supersaiakujin/items/be4a78809e7278c065e6
#   https://qiita.com/kenichiro_nishioka/items/8e307e164a4e0a279734
############################################################

class   Histogram:
    def __init__(self):
        pass

    def draw_graph(self, df, target):
        """
        :param df:データが格納されているDataFrame
        :param target: 表示するカラムのリスト
        :return:
        """
        color = ['tab:cyan', 'red', 'blue', 'green', 'yellow']
        x_min = min([df[col].min() for col in target])
        x_max = max([df[col].max() for col in target])
        data = [df[col] for col in target]
        bins = 10
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        ax.hist(data, bins=bins, color=color[:len(target)], range=(x_min, x_max), rwidth=0.9, label=target)
        ax.legend(loc='upper left')
        plt.show()
