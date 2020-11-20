# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:09:59 2020

@author: Ashwini.L
"""

import math
import numpy as np

Stock_Price = 72.72
Volatility = 0.3715
Risk_free_rate = 0.0697
numsim = 10
dt = [0.8333,1,1,1,1,0.8849]
numsteps = len(dt)

S = np.zeros([numsim,numsteps],dtype = float)

for i in range(numsteps):
    z = np.random.normal(size=numsim)
    if i == 0: 
        S[:,i] = Stock_Price * math.exp((Risk_free_rate - (Volatility**2)/2)*dt[i] + math.sqrt(dt[i])*Volatility*z[i])      
    else:
        S[:,i] = S[:,i-1] * math.exp((Risk_free_rate - (Volatility**2)/2)*dt[i] + math.sqrt(dt[i])*Volatility*z[i])

Stock      = S[:,5]
print(Stock)