# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:17:21 2017

@author: xiao
"""
import numpy as np

def GM_EM(x,K,times,e):
    # 初始化
    m,n = x.shape
    index,k_x = k_EM(x,K,times,e)
    a = np.ones((K,1))/1
    Cov = []
    new_k_x = np.zeros((K,n))
    new_Cov = []
    new_a = np.ones((K,1))/1
    P = lambda x,u,c: 1/(np.power((2 * np.pi),n/2) * np.sqrt(np.linalg.det(c)))* np.exp(-1/2 * np.dot(np.dot(x - u,np.linalg.pinv(c)),(x - u).T))
    for i in range(0,K):
        Cov.append(np.eye(n))
        new_Cov.append(np.eye(n))
    Cov = np.array(Cov)
    new_Cov = np.array(new_Cov)
    for t in range(0,times):
        # E算法
        gama = np.zeros((m,K))
        for j in range(0,m):
            p = np.zeros((K,1))
            for i in range(0,K):
                p[i] = P(x[j,:],k_x[i,:],Cov[i])
            gama[j,:] = a.T*p.T/np.dot(a.T,p)
               
        index = np.argmax(gama,axis = 1)
        y = index
        # M算法
        for i in range(0,K):
            new_k_x[i,:] = np.dot(gama[y == i,i].T,x[y == i,:])/np.sum(gama[y == i,i])
            new_Cov[i] = np.dot(((gama[y == i,i].reshape((len(gama[y == i,i]),1))) * (x[y == i,:] - k_x[i,:])).T,(x[y == i,:] - k_x[i,:]))/np.sum(gama[y == i,i])
            new_a[i] = 1/gama[y == i,:].shape[0] * np.sum(gama[y == i,i])
        if np.linalg.norm(new_k_x - k_x) < e and  np.linalg.norm(new_Cov - Cov) < e and np.linalg.norm(new_a - a) < e:
            break
        k_x = new_k_x
        Cov = new_Cov
        a = new_a
    return y,k_x
