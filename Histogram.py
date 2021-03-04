import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

############################################################
#
#   ヒストグラムを表示する
#
############################################################

class   Histogram:
    def __init__(self):
        pass

    def draw_graph(self, df, target):
        x_min = df[target].min()
        x_max = df[target].max()
        bins  = 10
        hist_data = plt.hist(df[target], bins=bins, color='tab:cyan', range=(x_min, x_max), rwidth=0.9)
        plt.show()