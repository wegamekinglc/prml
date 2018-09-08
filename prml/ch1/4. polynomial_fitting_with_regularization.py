# -*- coding: utf-8 -*-
"""
Created on 2018-9-8

@author: cheng.li
"""


if __name__ == '__main__':
    from prml.ch1.utilities import *
    from matplotlib import pyplot as plt
    sigma = 0.2
    lams = [math.exp(-18.), math.exp(0)]

    n_training = 10
    n_testing = 1000

    x1, y1 = create_curve(n_training)
    x2, y2 = create_curve(n_testing)
    y1 = add_noise(y1, sigma=sigma)

    fig, _ = plt.subplots(1, 2, sharex='all', sharey='all')
    fig.suptitle(r"Polynomials fitting with different regularization $M$ fitted to the curve $sin(2\pi x)$",
                 fontsize=15)
    for i, lam in enumerate(lams):
        beta = fitting(x1, y1, 9, lam=lam)
        y3 = fitted_curve(x2, beta)

        plt.subplot(120 + i + 1)
        plt.plot(x2, y2, 'g')
        plt.scatter(x1, y1, s=50, c='None', edgecolors='purple', linewidths=1)
        plt.plot(x2, y3, 'r')
        plt.text(0.8, 0.8, r"$\mathrm{{ln}} \ \lambda = {0}$".format(math.log(lam)))

    plt.show()