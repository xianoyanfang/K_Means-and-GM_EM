# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:02:32 2017

@author: xiao
"""
import numpy as np
import random


# k均值聚类
def k_EM(x,K,times,e):
    length = len(x)
    L = np.arange(0,length)
    random.shuffle(L)
    L = L[0:K]
    k_x = []
    for i in range(0,K):
       k_x.append(x[L[i],:])
    k_x = np.array(k_x)
    arg = np.zeros((K,1))
    for a in range(0,times):
        y = []
        old_x = k_x
        for i in range(0,length):
            for j in range(0,K):
                arg[j] = np.linalg.norm(x[i,:] - k_x[j,:])
            index = np.argmin(arg)
            y.append(index)
        y = np.array(y)
        for i in range(0,K):
            k_x[i,:] = np.sum(x[y == i,:],axis = 0)/x[y == i,:].shape[0]
        if np.linalg.norm(old_x - k_x) < e:
            break
    return y,k_x

