# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 22:15:11 2017

@author: yuwei
"""

#导入科学计算包
import numpy as np
#导入pandas      
import pandas as pd
#导入K-means算法包
from sklearn.cluster import KMeans
#导入时间包
import time
#导入聚类性能评价包
from sklearn import metrics

dataOld = pd.read_csv('replaceNaN.csv')
dataNew = pd.read_csv('MaxMinStandard.csv')

"原始数据集"
labels_true = dataOld['class']
#labels_true = np.array(data['class'])
#drop掉不需要使用的标签class
dataOld = dataOld.drop('class',axis=1).values
dataMat = np.mat(dataOld)
#跑聚类模型用到array类型
X = np.array(dataMat)
#调用聚类算法
y_pred = KMeans(n_clusters=8).fit_predict(X)
labels_pred = y_pred
#当前时间
t_o = time.time()
kmeans_model = KMeans(n_clusters=8).fit(X)
labels = kmeans_model.labels_
#计算模型训练所耗时间
t_batch_o = time.time() - t_o

"噪声处理后的数据集"
labels_true1 = dataNew['class']
#labels_true = np.array(data['class'])
#drop掉不需要使用的标签class
dataNew = dataNew.drop('class',axis=1).values
dataMat1 = np.mat(dataNew)
#跑聚类模型用到array类型
X1 = np.array(dataMat1)
#调用聚类算法
y_pred1 = KMeans(n_clusters=8).fit_predict(X1)
labels_pred1 = y_pred1
#当前时间
t_n = time.time()
kmeans_model1 = KMeans(n_clusters=8).fit(X1)
labels1 = kmeans_model1.labels_
#计算模型训练所耗时间
t_batch_n = time.time() - t_n

print "==============原始数据：Adjusted Rand index-评价指标=============="
print(metrics.adjusted_rand_score(labels_true, labels_pred))
print "========原始数据：Mutual Information based scores-评价指标========"
print(metrics.adjusted_mutual_info_score(labels_true, labels_pred))
print "====原始数据：Homogeneity, completeness and V-measure-评价指标===="
print(metrics.homogeneity_completeness_v_measure(labels_true, labels_pred))
print "============原始数据：Silhouette Coefficient-评价指标============="
print(metrics.silhouette_score(X, labels, metric='euclidean'))
print "---模型耗时---"
print(t_batch_o)

#print '\n'
print "********************************************************************"
print "********************************************************************"
#print '\n'

print "===========噪声处理后数据：Adjusted Rand index-评价指标==========="
print(metrics.adjusted_rand_score(labels_true1, labels_pred1))
print "======噪声处理后数据：Mutual Information based score-评价指标====="
print(metrics.adjusted_mutual_info_score(labels_true1, labels_pred1))
print "=噪声处理后数据：Homogeneity, completeness and V-measure-评价指标="
print(metrics.homogeneity_completeness_v_measure(labels_true1, labels_pred1))
print "=========噪声处理后数据：Silhouette Coefficient-评价指标=========="
print(metrics.silhouette_score(X1, labels1, metric='euclidean'))
print "---模型耗时---"
print(t_batch_n)

