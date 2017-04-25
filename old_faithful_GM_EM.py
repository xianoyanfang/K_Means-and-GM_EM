# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:09:32 2017

@author: xiao
"""
import numpy as np
import matplotlib.pyplot as plt
# 高斯混合聚类---老忠实数据
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
K = 2
times = 100
e = 1e-6
index,k_x = GM_EM(x,K,times,e)
plt.plot(x[index == 0,0],x[index == 0,1],'r.')
plt.plot(x[index == 1,0],x[index == 1,1],'b.')
str1 = 'K = ' +str(K)+',times = '+str(times)
plt.title(str1)