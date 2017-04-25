# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:24:05 2017

@author: xiao
"""

# 高斯混合聚类处理图像
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\xiao\.spyder-py3\机器学习\聚类\KMeans")

img = mpimg.imread('p.jpg')
head = img.shape
length = head[0]*head[1]
img = np.reshape(img,(length,3))
K = 2
times = 100
mean_img = np.mean(img,axis = 0)
std_img = np.std(img)
Data = (img - mean_img)/std_img
y,x = GM_EM(Data,K,times,1e-6)
x = x*std_img+mean_img
for i in range(0,K):
    img[y == i,:] = x[i,:]
A = np.reshape(img,(head[0],head[1],head[2]))
plt.imshow(A)
str1 = 'GM_EM K = ' +str(K)+',times = '+str(times)
plt.title(str1)