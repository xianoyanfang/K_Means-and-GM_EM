# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:16:55 2017

@author: xiao
"""

import numpy as np
import matplotlib.pyplot as plt
filename = r"C:\Users\xiao\.spyder-py3\机器学习\聚类\KMeans\old faithful.csv"
results = list()
file = open(filename, 'r')
reader = s=file.read().split()
k = 3
x = []
y = []
for i in range(0,272):
    x.append(float(reader[k]))
    y.append(float(reader[k+1]))
    k += 3
x = np.array(x)
y = np.array(y)
x = np.column_stack((x,y))
k = 2
times = 1000
index,k_x = k_EM(x,k,times,1e-6)
plt.plot(x[index == 0,0],x[index == 0,1],'r.')
plt.plot(x[index == 1,0],x[index == 1,1],'b.')

