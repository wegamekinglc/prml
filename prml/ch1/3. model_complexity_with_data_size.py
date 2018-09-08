# -*- coding: utf-8 -*-
"""
Created on 2018-9-8

@author: cheng.li
"""


if __name__ == '__main__':
    from prml.ch1.utilities import *
    from matplotlib import pyplot as plt
    sigma = 0.2
    orders = [0, 1, 3, 9]

    n_training1 = 15
    n_training2 = 100
    n_testing = 1000

    x1, y1 = create_curve(n_training1)
    x2, y2 = create_curve(n_training2)
    x3, y3 = create_curve(n_testing)
    y1 = add_noise(y1, sigma=sigma)
    y2 = add_noise(y2, sigma=sigma)

    data_sets = [(x1, y1), (x2, y2)]

    fig, _ = plt.subplots(1, 2, sharey='all')
    fig.suptitle("Polynomials fitting with different data set size", fontsize=15)
    for i, data in enumerate(data_sets):
        x, y = data
        beta = fitting(x, y, 9)
        y4 = fitted_curve(x3, beta)

        plt.subplot(120 + i + 1)
        plt.plot(x3, y3, 'g')
        plt.scatter(x, y, s=50, c='None', edgecolors='purple', linewidths=1)
        plt.plot(x3, y4, 'r')
        plt.text(0.8, 0.8, "$N = {0}$".format(len(x)))

    plt.show()
