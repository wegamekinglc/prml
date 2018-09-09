# -*- coding: utf-8 -*-
"""
Created on 2018-9-8

@author: cheng.li
"""


if __name__ == '__main__':
    from prml.ch1.utilities import *
    from matplotlib import pyplot as plt

    sigma = 0.2
    n_training = 15
    n_testing = 1000

    x1, y1 = create_curve(n_training)
    x2, y2 = create_curve(n_testing)
    y1 = add_noise(y1, sigma=sigma)
    y2 = add_noise(y2, sigma=sigma)

    lams = np.linspace(-50, 0, 11)
    rms_training = []
    rms_testing = []
    for lam in lams:
        beta = fitting(x1, y1, 9, lam=math.exp(lam))
        y1_hat = fitted_curve(x1, beta)
        rms_training.append(rms(y1, y1_hat))
        y2_hat = fitted_curve(x2, beta)
        rms_testing.append(rms(y2, y2_hat))

    plt.plot(lams, rms_training, '-b', marker='o', markersize=10, markerfacecolor='None')
    plt.plot(lams, rms_testing, '-r', marker='o', markersize=10,  markerfacecolor='None')
    plt.legend(['Training', 'Testing'], handlelength=5)
    plt.ylabel('$E_{RMS}$')
    plt.xlabel('$\mathrm{{ln}} \ \lambda$')
    plt.title("Training v.s. Testing with root-mean-square error", fontsize=15)
    plt.show()
