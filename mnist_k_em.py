# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:49:38 2017

@author: xiao
"""
# 手写数字10聚类
K = 10
times = 5000
y,k_x = k_EM(Train_x,K,times,1e-6)
m,n = Test_x.shape
pre_y = []
arg = np.zeros((K,1))
for i in range(0,m):
    for j in range(0,K):
        arg[j] = np.linalg.norm(Test_x[i,:] - k_x[j,:])
    index = np.argmin(arg)
    pre_y.append(index)
pre_y = np.array(pre_y)
accuary = 1 - np.sum(pre_y != Test_y)/m
print('accuary = ',accuary)