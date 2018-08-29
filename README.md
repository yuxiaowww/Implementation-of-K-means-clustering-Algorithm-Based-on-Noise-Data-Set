# Implementation-of-K-means-clustering-Algorithm-Based-on-Noise-Data-Set
## 1、对于UCI 数据集：Mice Protein Expression Data Set进行无噪声处理和进行噪声处理，对这两个数据集，分别进行K-means聚类算法进行实验；
## 2、调用四种聚类性能评价指标：分别是Adjusted Rand index、Mutual Information based scores、Homogeneity, completeness and V-measure、Silhouette Coefficient；
## 3、实验结论：除了轮廓系数（Silhouette Coefficient）在去躁后效果低于去躁前，其余聚类评价指标均有提升，并且在建模时间上也有明显提升，因此，可以知道，噪声数据对聚类结果影响很大。
## 执行：code中四个文件，按顺序依次执行即可，数据集存放在当前文件路径。
## 缺点：因为是本科毕设，所以去躁可应用性很弱。
