# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 22:15:11 2017

@author: yuwei
"""

#科学计算包
import numpy as np
#python画图包      
import matplotlib.pyplot as plt      
#导入K-means算法包
from sklearn.cluster import KMeans
#导入时间包
import time 

#figure函数设置绘图框的大小
plt.figure(figsize=(6, 6))
#函数作用：将文本文件读入一个列表中
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        #按每行读入，tab分割
        curLine = line.strip().split(',')
        #map()为Python内置的高阶函数，接受f和list，f依次作用于list，返回list
        fltLine = map(float,curLine)
        dataMat.append(fltLine)
    return dataMat
dataMat = np.mat(loadDataSet('StandardOfZscore.csv'))
X = np.array(dataMat)
#当前时间
t0 = time.time()
#调用k-means算法库 
y_pred = KMeans(n_clusters=4).fit_predict(X)
#训练模型，为了找出聚类中心
y = KMeans(n_clusters=4).fit(X)
clusterCenter = y.cluster_centers_
#计算模型训练所耗时间
t_batch = time.time() - t0  
plt.subplot(111)
#scatter绘制散点
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
#绘制聚类中心的四个点
plt.scatter(clusterCenter[:,0],clusterCenter[:,1],c='r',marker='x')
#加标题
plt.title("Sklearn-KMeans:Draw Fig to Cluster 4 Category")
#设置X轴标签  
plt.xlabel('X')  
#设置Y轴标签  
plt.ylabel('Y')
#显示绘制的散点图
plt.show()
#显示建模所耗时间
print '建模耗时：'
print(t_batch)

