# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 16:43:49 2017

@author: yuwei
"""

'''
对聚类模型做评价
'''


from sklearn import metrics

"指标对称-评价指标"
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [0, 0, 1, 1, 2, 2]
print(metrics.adjusted_rand_score(labels_true, labels_pred))#0.24
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [1, 1, 1, 0, 0, 0]
print(metrics.adjusted_rand_score(labels_true, labels_pred))#1.0

"相互信息-评价指标"
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [0, 0, 1, 1, 2, 2]
print(metrics.adjusted_mutual_info_score(labels_true, labels_pred))#0.24
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [1, 1, 1, 0, 0, 0]
print(metrics.adjusted_mutual_info_score(labels_true, labels_pred))#1.0

"均匀性，完整性、V度量-评价指标"
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [0, 0, 1, 1, 2, 2]
print(metrics.homogeneity_completeness_v_measure(labels_true, labels_pred))#0.24
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [1, 1, 1, 0, 0, 0]
print(metrics.homogeneity_completeness_v_measure(labels_true, labels_pred))#1.0

"Silhouette Coefficient"
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import datasets
dataset = datasets.load_iris()
X = dataset.data
y = dataset.target
import numpy as np
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
labels = kmeans_model.labels_
print(metrics.silhouette_score(X, labels, metric='euclidean'))


'''
"Fowlkes-Mallows scores"
from sklearn import metrics
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [0, 0, 1, 1, 2, 2]
print(metrics.fowlkes_mallows_score(labels_true, labels_pred))#0.24
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [1, 1, 1, 0, 0, 0]
print(metrics.fowlkes_mallows_score(labels_true, labels_pred))#1.0


"Calinski-Harabaz Index"
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import datasets
dataset = datasets.load_iris()
X = dataset.data
y = dataset.target
import numpy as np
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
labels = kmeans_model.labels_
print(metrics.calinski_harabaz_score(X, labels))
'''







