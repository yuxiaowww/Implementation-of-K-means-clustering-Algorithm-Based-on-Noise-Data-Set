# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 16:12:58 2017

@author: yuwei
"""

"""
0、删除小白鼠的ID，以及Genotype、Treatment、Behavior;
1、为了便于比较分类效果，将class字符串类型转换为数值型：0-7;
2、为了方便处理（NaN类型通常不利于处理），将数据中所有空值替换为0;
3、将含有空值的列取出，求得其均值，并用均值替换空值的位置;
4、由于空值已经利用均值替换，因此这里不能使用z-Score做归一化处理，使用Max-Min归一化处理
"""

import pandas as pd

#导入原始数据集
data = pd.read_excel('testData.xls')
#删除无关序列Genotype、Treatment、Behavior
del data['MouseID']
del data['Genotype']
del data['Treatment']
del data['Behavior']
#查看class中共分为了几类，set为集合可以去除重复
print(set(data['class']))
#转为class类型为0,1,2,3,4,5,6,7
data['class'][data['class'] == 'c-SC-s'] = '0'
data['class'][data['class'] == 't-SC-m'] = '1'
data['class'][data['class'] == 't-CS-m'] = '2'
data['class'][data['class'] == 'c-SC-m'] = '3'
data['class'][data['class'] == 'c-CS-s'] = '4'
data['class'][data['class'] == 'c-CS-m'] = '5'
data['class'][data['class'] == 't-SC-s'] = '6'
data['class'][data['class'] == 't-CS-s'] = '7'

data.to_csv('dealedData.csv',index=False)
#将数据中所有空值替换掉，导出数据文件
data.replace(to_replace='NaN', value=0, regex=True, inplace=True)
data.to_csv('replaceNaN.csv',index=False)
'''
'''
#将属性标签编号为顺序的
data1 = pd.read_csv('replaceNaN_order.csv')
#循环为噪声数据赋值
for i in range(0,77):
    data1[str(i)][data1[str(i)] == 0] = data1[str(i)].mean()

data1.to_csv('replaceNaN_test_meanR.csv',index=False)


#数据进行最大最小归一化
data2 = pd.read_csv('replaceNaN_test_meanR.csv')
length = len(data2['0'])
#循环为噪声数据赋值
for i in range(0,77):
    minum = data2[str(i)].min()
    maxium = data2[str(i)].max()
    #mean = data2[str(i)].mean()
    for j in range(0,length):
        print(i,j)
        data2[str(i)].iloc[j] = (data2[str(i)].iloc[j] - minum)/(maxium - minum)

data2.to_csv('MaxMinStandard.csv',index=False)

