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
    for o in range(order + 1):
        x_mat[:, o] = np.power(x, o)
    return x_mat


def fitting(x, y, order, lam=0.):
    m = order + 1
    x_mat = polynomials(x, order)
    h = np.linalg.inv(x_mat.T @ x_mat + np.diag(lam * np.ones(m))) @ x_mat.T
    beta = h @ y
    return beta


def fitted_curve(x, beta):
    order = len(beta) - 1
    x_mat = polynomials(x, order)
    y_hat = x_mat @ beta
    return y_hat


def rms(y, y_hat):
    n = len(y)
    return math.sqrt(np.sum((y - y_hat) ** 2) / n)
