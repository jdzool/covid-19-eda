#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:27:51 2020

@author: jon.downing

Fitting functions and graphs to explore the growth 
of COVID-19 in the UK 

Using deaths a measure for progress

You can undersample on infection rate but 
undersampling deaths is a lot more difficult 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from datetime import timedelta
from matplotlib.dates import DateFormatter
from datetime import datetime
import os 

from funcs.functions import exponential_func


"""
-- Get Data -- 

New data is released from here daily: 
https://www.arcgis.com/home/item.html?id=e5fd11150d274bebaaf8fe2a7a2bda11
"""
path = r'./data/DailyConfirmedCases.xlsx'

# Read data
data = pd.read_excel(path)

# Create an index column 
data["day_number"] = list(range(0,len(data)))

# Today's date as string -- we'll use this later 
now = datetime.now()
date_today = now.strftime("%Y-%m-%d")

"""
The data set is from 31st January where there are relatively few cases
Lets start fitting from mid-Feb. There is little change in the initial cases
in early Feb and we want our fit to be accurate in the growth period. 
"""
start_day_index = 55 # Change here to modify plots

x = data.day_number.to_numpy()[start_day_index:] 
y = data.CumDeaths.to_numpy()[start_day_index:]

# Use a function to fit the data 
# Provide bounds on the fitting function 
popt, pcov = curve_fit(exponential_func, x, y, bounds=(-1, [4000., 0.5, 30]))

"""
popt --> array (Optimal values for the parameters so 
that the sum of the squared residuals of f(xdata, *popt) - ydata is minimized)

pcov2d --> array (The estimated covariance of popt.)
"""

# What are fitting co-efficients / variables 
#print( "B = %s , M = %s, H = %s, R = %s" % (popt[0], popt[1], popt[2], popt[3]))

# Prepare data for plotting 

# We need the same length for everything 
dates = data.DateVal[start_day_index:]

# matplotlib likes datetimes, convert from pandas timestamp format 
x_dates = [datetime.strptime(str(y), '%Y-%m-%d %H:%M:%S') for y in dates]

# Create the prediction dataset 
n = 5 # How many future days 

# create array with future datetimes
dates_future = [dates.iloc[-1] + timedelta(days=x) for x in range(1, n)]
x_dates_future = [datetime.strptime(str(y), '%Y-%m-%d %H:%M:%S') for y in dates_future]

# create 
x_future = np.array(list(range(x[-1]+1,x[-1] + n)))

"""
Create error profile 
"""

perr = np.sqrt(np.diag(pcov))

"""
-- Plotting -- 

2 Plots, 3 data sets: 
Left plot - linear
Right plot - logarithmic 

Datasets: 
measured data, fitted curve, prediction for next 10 days 
"""

# Subplot setup
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
fig.suptitle('Number of COVID-19 deaths \n (UK population)')
ax1.set(xlabel="Date")
ax1.set(ylabel="Confirmed deaths (COVID-19) UK")
ax1.legend(loc='upper left')
ax2.set_yscale("log")
ax2.set(xlabel="Date")

dateFmt = DateFormatter(r'%a %d %b %y') # Used for the x-axis format 

# if plot folder doesn't exist, make it
if not os.path.exists(r"./plots/"):
    os.makedirs("./plots/")

# create plots
for ax in (ax1, ax2): 
    # Add measured data 
    ax.plot(x_dates, y, 'ko', label="Daily Confirmed Cumulative Deaths")
    
    # Add fit
    ax.plot(x_dates, exponential_func(x, *popt), 'r-', label="Logistic Fit")
    
    # Add prediction
    ax.plot(x_dates_future, exponential_func(x_future, *popt), 'bo', label="Prediction")
    
    # Add error
    ax.plot(x_dates_future, exponential_func(x_future, *perr), label="Prediction Error")
     
    # Some more formatting 
    plt.setp( ax.xaxis.get_majorticklabels(), rotation=90 ) 
    ax.xaxis.set_major_formatter(dateFmt)


# tight_layout is needed to make the plot look nioce. 
plt.tight_layout(rect=[0, 0.03, 1, 0.9])
ax1.legend(loc='upper left')

# Save! 
fig.savefig(os.path.join(r'./plots/', date_today + '_corona_virus_fit_deaths.png'), format = 'png', dpi = 400)






