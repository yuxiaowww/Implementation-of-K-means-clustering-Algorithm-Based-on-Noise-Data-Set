# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:03:31 2017

@author: yuwei
"""


from numpy import *
#python画图包      
import matplotlib.pyplot as plt
#导入时间包
import time

def loadDataSet(fileName):
    "将文本文件读入一个列表中"
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        #按每行读入，tab分割
        curLine = line.strip().split(',')
        #map()为Python内置的高阶函数，接受f和list，f依次作用于list，返回list
        fltLine = map(float,curLine)
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA,vecB):
    "计算两个向量之间的欧式距离的三种实现方式"
    return sqrt(sum(power(vecA - vecB,2)))
    #return numpy.sqrt(numpy.sum(numpy.square(vecA - vecB)))  
    #return numpy.linalg.norm(vecA - vecB)  

def randCent(dataSet, k):
    "构建随机质心"
    #n保存dataSet一共多少行数据
    n = shape(dataSet)[1]
    #centriods建立一个k行n列的0矩阵
    centriods = mat(zeros((k,n)))
    for j in range(n):
        #minJ存储第j行中最小值，可以使用tuple是因为dataSet已经强制转为矩阵形式
        #minJ = min(dataSet[:][j])
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centriods[:,j] = minJ + rangeJ*random.rand(k,1)
    return centriods

dataMat = mat(loadDataSet('StandardOfZscore.csv'))
#print(dataMat)
#print(dataMat)
#print '\n'
#print 'min(dataMat[:,0])'
#print min(dataMat[:,0])
#print 'min(dataMat[:,1])'
#print min(dataMat[:,1])
#print 'max(dataMat[:,0])'
#print max(dataMat[:,0])
#print 'max(dataMat[:,1])'
#print max(dataMat[:,1])
#
#centriod = randCent(dataMat,2)
#print '测试随机质心：'
#print centriod
#
#print '测试欧式距离：'
#print distEclud(dataMat[0],dataMat[1])
#print '\n'

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    #m指数据文件的总长度
    m = shape(dataSet)[0]
    print(m)
    #分配一个矩阵存储数据，包括质心以及每个数据点
    clusterAssment = mat(zeros((m,2))) 
    #生成随机质心                                  
    centroids = createCent(dataSet, k)
    #聚类中心是否改变的标记
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        #对于每个数据点，将其分配给最接近的的质心
        for i in range(m):#循环整个数据的长度
            #inf为无穷大，minIndex标记索引值
            minDist = inf; minIndex = -1
            for j in range(k):#循环簇的个数
                #计算质心和数据点之间的欧式距离
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    #赋值最小距离和此时的索引
                    minDist = distJI; minIndex = j
            #如果簇归类不等于此时的最小索引，意味着聚类还在改变，继续标记需要循环
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            #循环结束，就赋值簇列表
            clusterAssment[i,:] = minIndex,minDist**2
        #print centroids
        #重新计算簇中心
        for cent in range(k):
            #得到这个簇中所有的点，去掉第一列等于cent的所有列
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            #指定簇中心的平均值
            centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment
    
#当前时间
t0 = time.time()   
myCentroids, clusterAssing = kMeans(dataMat,4)
#计算模型训练所耗时间
t_batch = time.time() - t0

print '聚类中心：'
print myCentroids
print '聚类结果：'
print clusterAssing
  
##figure函数设置绘图框的大小
#plt.figure(figsize=(6, 6))
##在图中1的位置里添加子图1
#plt.subplot(111)  
##scatter绘制散点，按数据第一列、第二列，为散点图的x,y坐标，以及聚类后的簇结果为点的颜色，绘制聚类散点结果图
#plt.scatter(array(dataMat[:,0]), array(dataMat[:,1]), c=array(clusterAssing[:,0]))
##四个类的聚类中为x，y轴，颜色为红色，形状为diamond，绘制聚类中心
#plt.scatter(array(myCentroids[:,0]), array(myCentroids[:,1]), c='r',marker='D')
##给散点图加标题
#plt.title("My-KMeans:Draw Fig to Cluster 4 Category")
##设置X轴标签  
#plt.xlabel('X')  
##设置Y轴标签  
#plt.ylabel('Y')
##显示绘制的散点图
#plt.show()
##显示建模所耗时间
#print '建模耗时：'
#print(t_batch)
