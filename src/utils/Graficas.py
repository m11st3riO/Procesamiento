import numpy as np
import matplotlib.pyplot as plt


def Grap_s(t,f,a):
    return a * np.sin(2 * np.pi * f * t)

def Grap_e(t):
    return np.exp(-2 * t) * (t >= 0)

def Grap_t(t,f,):
    p = 1/f

    t_norm = (t % p) / p
    
    return 4 * np.abs(t_norm - 0.5) - 1

def Grap_c(t,f,):

    return np.where(np.sin(2 * np.pi * f * t) >= 0, 1, -1)

