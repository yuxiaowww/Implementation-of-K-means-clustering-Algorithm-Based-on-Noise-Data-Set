# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 22:15:11 2017

@author: yuwei
"""

#导入科学计算包
import numpy as np
#导入python画图包      
import matplotlib.pyplot as plt      
#从sklearn中导入K-means算法包
from sklearn.cluster import KMeans
#导入make_blobs生成随机数据集       
from sklearn.datasets import make_blobs

#设置绘图大小
plt.figure(figsize=(12, 12))
#表示数据样本点个数,默认值100
n_samples = 500
#官网解释是随机生成器的种子
random_state = 170
#make_blobs其他参数解释
'''
make_blobs函数是为聚类产生数据集产生一个数据集和相应的标签
n_features:表示数据的维度，默认值是2
centers:产生数据的中心点，也相当于生成centers个簇，默认值3
cluster_std：数据集的标准差，浮点数或者浮点数序列，默认值1.0
center_box：中心确定之后的数据边界，默认值(-10.0, 10.0)
shuffle ：洗乱，默认值是True
'''
#调用make_blobs函数生成数据集
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

"调用sklearn中的kMeans函数"
'''
这个例子是为了说明k-means会产生的情况:不直观的和意想不到的群集；
在前三个例子中，输入数据为不符合k-means的隐含的假设因此产生不期望的簇； 
在最后的情节，k-means尽管不均匀大小的斑点，仍返回直观的群集。
'''
#图1：聚类集群数不正确
y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)
#在2*2格式的图里第一个位置添加子图1
plt.subplot(221)
#scatter绘制散点  
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
#加标题
plt.title("Incorrect number of clusters")

#图2：非均匀分布式数据
#transformation = [[ 0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
transformation = [[ 0.4, -0.4], [-0.6, 0.12]]
#计算X与transformation的乘积
X_aniso = np.dot(X, transformation)
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_aniso)
#在2*2格式的图里第二个位置添加子图2
plt.subplot(222)
plt.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
plt.title("Anisotropicly Distributed Blobs")

#图3：不同的方差
X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],#设置不同的方差
                                random_state=random_state)
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)
#在2*2格式的图里第二个位置添加子图3
plt.subplot(223)
plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
plt.title("Unequal Variance")

#图4：大小不一的聚类簇
#y一共有三类：0,1,2 分别选取0类中的前500,1类中的前100，2类中的前10，然后合并在一起作为训练数据
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_filtered)
#在2*2格式的图里第二个位置添加子图4
plt.subplot(224)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs")

#显示绘图的结果
plt.show()
