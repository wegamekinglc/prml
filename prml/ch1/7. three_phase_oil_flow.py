# -*- coding: utf-8 -*-
"""
Created on 2018-9-9

@author: cheng.li
"""

if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt

    df1 = pd.read_table("../data/three_phase_oil_flow/DataTrn.txt", header=None)
    df2 = pd.read_table("../data/three_phase_oil_flow/DataTrnLbls.txt", header=None)
    del df1[12]
    del df2[3]

    cols = np.array(df2.columns)
    labels = df2.values @ cols

    df1['c'] = labels
    colors = list(map(lambda x: 'r' if x == 0 else 'g' if x == 1 else 'b', df1['c']))
    plt.scatter(df1[5], df1[6], c='None', edgecolors=colors)
    plt.xlabel('$x_6$')
    plt.ylabel('$x_7$')
    plt.xlim([0., 1.])
    plt.ylim([0., 2.])
    plt.show()
