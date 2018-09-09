# -*- coding: utf-8 -*-
"""
Created on 2018-9-9

@author: cheng.li
"""

if __name__ == '__main__':
    from prml.ch1.utilities import *
    from matplotlib import pyplot as plt

    sigma = 0.3
    n_training = 10
    n_testing = 1000
    order = 9
    alpha = 0.005
    beta = 1. / (sigma ** 2)

    x1, y1 = create_curve(n_training)
    y1 = add_noise(y1, sigma=sigma)
    x2, y2 = create_curve(n_testing)

    fitter = BayesianFitter(x1, y1, order, alpha, beta)
    fitter.fitting()
    m, var = fitter.predict(x2)
    std = np.sqrt(var)

    plt.plot(x2, m, 'g')
    plt.scatter(x1, y1, s=50, c='None', edgecolors='purple', linewidths=1)
    plt.plot(x2, y2, 'r')
    plt.fill_between(x2, m - std, m + std, facecolor='salmon', alpha=0.4)
    plt.xlabel('x')
    plt.ylabel('t')
    plt.show()