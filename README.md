# K_EM
python sklearn模块有聚类这一块的函数，在这里利用聚类的算法原理手动实现一遍 （老子要开干啦╭(╯3╰)╮) <br>
## k_EM.py
k_EM.py 里面包含k均值聚类函数k_EM(x,K,times,e)，返回值是y,k_x<br>
* x 要训练的数据<br>
* K 聚类类别个数<br>
* times 内部循环的最多次数<br>
* e 聚类的误差小于 e 则退出循环<br>
## get_MNIST.py
获取 mnist 手写数字<br>
数据集可以在 LSC 文件夹中获取
## mnist_k_em.py
对手写数字 mnist 进行10均值聚类，结果正确率为 accuary = 0.20079999999999998<br>
## k_EM_img.py
将图片进行颜色聚类<br>
'在图片聚类时也能够加入像素点的位置，不过要考虑的一点就是需要对训练集进行归一化'<br>

# 实现
这里实现了mnist手写数字10分类<br>
图片聚类<br>
老忠实数据2聚类<br>
# GM_EM
## GM_EM.py
GM_EM.py 高斯混合聚类的算法实现，为函数GM_EM(x,K,times,e)<br>
* x 进行聚类的数据<br>
* K 聚类的类别数<br>
* times 内部进行循环的最大轮数<br>
* e 误差终止条件<br>
## old_faithful_GM_EM.py
老忠实数据进行高斯混合聚类，显然效果比K均值聚类效果佳<br>
内部可以设置聚类类别数 K 和最大轮数 times 以及终止误差 e<br>
## GM_EM_img.py
利用高斯混合聚类对图像进行聚类<br>
注意：由于像素点数据是在0-225之间，数据过大，在这里将数据进行标准化之后进行高斯混合聚类


## 特别注意:
这里程序运行都是有顺序的，1. k_EM.py 2. GM_EM.py 这两个都是定义了聚类的算法的核心函数，故最先运行<br>
如果要运行手写数字的话需要先运行 get_MNIST.py 文件，其中数据集可以从LSC文件夹中获取，之后在运行mnist_k_em.py 或 mnist_gm_em.py文件
