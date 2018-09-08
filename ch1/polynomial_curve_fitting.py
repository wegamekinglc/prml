# -*- coding: utf-8 -*-
"""
Created on 2018-9-8

@author: cheng.li
"""

import math
import numpy as np


def create_curve(n):
    x = np.linspace(0., 1., num=n)
    y = np.sin(2. * math.pi * x)
    return x, y
    

def add_noise(y, sigma=0.01):
    y_hat = y + np.random.randn(len(y)) * sigma
    return y_hat


def polynomials(x, order):
    x_mat = np.zeros((len(x), order + 1))
    for o in range(order+1):
        x_mat[:, o] = np.power(x, o)
    return x_mat


def fitting(x, y, order):
    x_mat = polynomials(x, order)
    h = np.linalg.inv(x_mat.T @ x_mat) @ x_mat.T
    beta = h @ y
    return beta


def fitted_curve(x, beta):
    order = len(beta) - 1
    x_mat = polynomials(x, order)
    y_hat = x_mat @ beta
    return y_hat


if __name__ == '__main__':
    from matplotlib import pyplot as plt
    sigma = 0.2
    orders = [0, 1, 3, 9]

    n_training = 10
    n_testing = 1000

    x1, y1 = create_curve(n_training)
    x2, y2 = create_curve(n_testing)
    y1 = add_noise(y1, sigma=sigma)

    fig, _ = plt.subplots(2, 2, sharex='all', sharey='all')
    fig.suptitle(r"Plots of polynomials having various orders $M$ fitted to the curve $sin(2\pi x)$", fontsize=15)
    for i, order in enumerate(orders):
        beta = fitting(x1, y1, order)
        y3 = fitted_curve(x2, beta)

        plt.subplot(220 + i + 1)
        plt.plot(x2, y2, 'g')
        plt.scatter(x1, y1, s=50, c='', edgecolors='purple', linewidths=1)
        plt.plot(x2, y3, 'r')
        plt.text(0.8, 0.8, "$M = {0}$".format(order))

    plt.show()
