# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:19:40 2017

@author: xiao
"""
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\xiao\.spyder-py3\机器学习\聚类\KMeans")

img = mpimg.imread('p.jpg')
head = img.shape
length = head[0]*head[1]
img = np.reshape(img,(length,3))
K = 3
times = 1000
y,x = k_EM(img,K,times,1e-6)
for i in range(0,K):
    img[y == i,:] = x[i,:]
A = np.reshape(img,(head[0],head[1],head[2]))
plt.imshow(A)
str1 = 'K = ' +str(K)+',times = '+str(times)
plt.title(str1)