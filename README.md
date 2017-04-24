# K_EM
## k_EM.py
k_EM.py 里面包含k均值聚类函数k_EM(x,K,times,e)，返回值是y,k_x<br>
* x 要训练的数据<br>
* K 聚类类别个数<br>
* times 内部循环的最多次数<br>
* e 聚类的误差小于 e 则退出循环<br>
## get_MNIST.py
获取 mnist 手写数字<br>
## mnist_k_em.py
对手写数字 mnist 进行10均值聚类，结果正确率为 accuary = 0.20079999999999998<br>
## k_EM_img.py
将图片进行颜色聚类<br>
'在图片聚类时也能够加入像素点的位置，不过要考虑的一点就是需要对训练集进行归一化'<br>
