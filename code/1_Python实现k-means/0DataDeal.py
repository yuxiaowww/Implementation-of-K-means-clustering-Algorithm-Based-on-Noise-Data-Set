# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 13:17:49 2017

@author: yuwei
"""

#ecoding=utf-8  
import math  
from numpy import *
from pandas import DataFrame
import pandas as pd
    
def fileREAD(fileURL,access):  
    "传入文件路径，返回存储文件内容的二维列表"  
    localArray = []  #创建一个列表用于存储文件内容
    #传入文件路径与打开模式
    csvfile = file(fileURL, access)
    #读取文件的行
    reader = csvfile.readlines()  
    for line in reader:
        #按tab键分割
        curLine = line.strip().split('\t')
        localArray.append(curLine)  
    csvfile.close()  
    return localArray
#把返回的存储文件存放在inList中
inList = fileREAD('testSet.csv','r')
#强制转型为DataFrame类型，方便取值计算
dataF = DataFrame(inList)
#分别存储第一列和第二列
Mat0 = dataF[0]
Mat1 = dataF[1]

def getAVG(Mat):
    "求数值属性的均值"
    sumOfList = 0 #存储该列的总和
    lengthOfList = 0 #存储该列的长度
    for i in range(len(Mat)):
        #循环求和与长度
        sumOfList = sumOfList + float(Mat[i])
        lengthOfList = lengthOfList + 1
    if lengthOfList != 0 :
        #返回均值
        return sumOfList/lengthOfList
    else:
        return '无均值'
#分别计算两列的均值
averageX = getAVG(Mat0)
averageY = getAVG(Mat1)
average = []
average.append(averageX)
average.append(averageY)
print('均值为：')
print(average)

def getAVE(Mat,average):
    "计算标准差"
    standDev = 0
    lengthOfList = 0
    for i in range(len(Mat)):
        #首先计算各值与均值差值的平方和，以及总长度
        standDev = standDev + pow(float(Mat[i]) - average,2)
        lengthOfList = lengthOfList + 1
    if lengthOfList != 0:
        return math.sqrt(standDev/lengthOfList)
    else:
        return '无标准差'
#分别计算两列的标准差
standDevX = getAVE(Mat0,averageX)        
standDevY = getAVE(Mat1,averageY)
standDev = []
standDev.append(standDevX)
standDev.append(standDevY)
print('标准差为：')
print(standDev)

def  zScore(Mat,average,standDev):  
    "zScore归一化,(x-均值)/标准差"    
    for i in range(len(Mat)):  
        a = (float(Mat[i])-average)/standDev
        Mat[i] = '%.4f' % a
    return Mat  
FirstRow = zScore(Mat0,average[0],standDev[0])
SecondRow = zScore(Mat1,average[1],standDev[1])
FirstRow = DataFrame(FirstRow)
SecondRow = DataFrame(SecondRow)
FirstRow.to_csv('FirstRow.csv',index=True)
SecondRow.to_csv('SecondRow.csv',index=True)
FirstRow = pd.read_csv('FirstRow.csv',names=['order','label'])
SecondRow = pd.read_csv('SecondRow.csv',names=['order','label'])
#merge两列处理好的数据
StandardOfZscore = pd.merge(FirstRow,SecondRow,on=['order'])
#删除order列，order列为连接两列数据的根据，已经为无关序列
del StandardOfZscore['order']
#drop掉产生的第一行的索引行
StandardOfZscore.drop(StandardOfZscore.index[[0]],inplace=True)
#StandardOfZscore = StandardOfZscore.drop(0)
#导出数据
StandardOfZscore.to_csv('StandardOfZscore.csv',index=False,header=False)
