
import numpy as np 


def exponential_func(x, a, b, c):
    """
    An exponential only explains the growth. There should be a 
    tapering towards the peak and eventually a fall. 
    """
    return a * np.exp(b * x) + c



def logistic_func(x, m, b, a):
    """
    The three parameter logistic growth curve proposed by Heuvel (2020) (see /papers)
    could not fit this curve. 
    """
    return m / (1 + np.exp(-b * (x - a)))


def logistic_func_2(x, B, M, H, R):
    """
    Another logistic type formula. This has more parameters so is a weaker fit.
    At times this has been required to fit the data
    """
    return B + M / (np.exp((H - x)/R))

def calc_st_dev(pcov):
    """
    pcov = Covariance matrix
    variance is the diagonal elements of the matrix
    standard deviation is root of the variance 

    Or just use this --> perr = np.sqrt(np.diag(pcov))
    """
    standard_deviations = []
    for i in range(0,len(pcov)): 
        standard_deviations.append(pcov[i,i]**0.5)
    
    return standard_deviations