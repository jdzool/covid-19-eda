
import numpy as np 

"""
An exponential only explains the growth. There should be a 
tapering towards the peak and eventually a fall
"""
def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

"""
The three parameter logistic growth curve proposed by Heuvel (2020) (see /papers)
could not fit this curve. 
"""
def logistic_func(x, m, b, a):
    return m / (1 + np.exp(-b * (x - a)))

"""
Another logistic type formula. Need to read the literature 

This has more parameters so is a weaker fit.
"""
def logistic_func_2(x, B, M, H, R):
    return B + M / (np.exp((H - x)/R))

"""
"""