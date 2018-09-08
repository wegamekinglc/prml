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

    n_training = 10
    n_testing = 1000

    x1, y1 = create_curve(n_training)
    x2, y2 = create_curve(n_testing)
    y1 = add_noise(y1, sigma=sigma)

    fig, _ = plt.subplots(2, 2, sharex='all', sharey='all')
    fig.suptitle(r"Polynomials having various orders $M$ fitted to the curve $sin(2\pi x)$", fontsize=15)
    for i, order in enumerate(orders):
        beta = fitting(x1, y1, order)
        y3 = fitted_curve(x2, beta)

        plt.subplot(220 + i + 1)
        plt.plot(x2, y2, 'g')
        plt.scatter(x1, y1, s=50, c='None', edgecolors='purple', linewidths=1)
        plt.plot(x2, y3, 'r')
        plt.text(0.8, 0.8, "$M = {0}$".format(order))

    plt.show()
