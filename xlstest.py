#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'tl'

import xlsxwriter as wx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # 创建文件
# workbook = wx.Workbook('hello.xlsx')
# # 增加sheet表
# worksheet = workbook.add_worksheet()
# # 设置列宽
# worksheet.set_column('A:A',len('hello world')+1)
# # 写入数据
# worksheet.write(0,0,'hello world')
# # 关闭文件
# workbook.close()


# workbook = wx.Workbook('hello.xlsx')
# worksheet1 = workbook.add_worksheet(name='images1')
# worksheet2 = workbook.add_worksheet(name='images')
# worksheet1.set_column('A:A',30)
# worksheet1.write('A2','Insert an image in a cell: ')
# worksheet1.insert_image('B2','python.png',{'x_scale':0.4,'y_scale':0.4})
# worksheet1.write('A12','Insert a scaled image: ')
# worksheet1.insert_image('B12','python.png',{'x_scale':0.2,'y_scale':0.2})
# workbook.close()

'''
以下为pandas示例，参考以下博客内容
http://blog.csdn.net/qq_14959801/article/details/51422913
http://www.jb51.net/article/63216.htm
'''
s = pd.Series([1,3,5,np.nan,6,8])
# print s
dates = pd.date_range('20160501',periods=6)
# print dates
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# print df
df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20160501'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
# print df2
# print df2.dtypes
# print df.head()
# print df.tail(3)
# print df.index
# print df.values
# print df.describe()
# print df.T
# print df.sort_index(axis=1,ascending=False)   #以横向索引降序排列
# print df.sort_index(axis=0,ascending=False)   #以纵向索引降序排列
# print df['A']   #只统计A索引列
# print df[0:3]   #统计1至3行数据
# print df['20160502':'20160504']  #以date_rage索引统计指定行数据
# print df.loc[dates[1]]      #以日期截取行
# print df.loc[dates[1],'A']      #以日期截取行，并指定列
# print df.loc[:,['A','B']]   #以日期截取所有行，并截取指定列
# print df.loc['20160502':'20160504',:]       #以日期截取指定行，并截取所有列
# print df.iloc[5]                #根据行数直指行数据
# print df.iloc[4:6,0:2]          #iloc直接确定行列数
# print df[df.A>0]                #显示A列大于0的行数
# print df[df>0]                  #只显示大于零的数值

# df2 = df.copy()                   #拷贝，默认深拷贝
# df2['E']=['one','one','two','three','four','three']         #增加一个索引为E的列，并赋值
# print df2[df2['E'].isin(['two','four'])]    #显示E列为'two','four'的行
# s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20160501',periods=6))
# # print s1
# df['F'] = s1                        #将S1的列值赋值给df的索引为F的列
# df.at[dates[0],'A'] = 0            #将第一行，A列对应的值修改为0
# df.loc[:,'D'] = np.array([5]*len(df))   #将D列替换为5
# df.iat[0,1] = 0                     #iat直接确定行列
# del df['F']                         #删除F列
# s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20160502',periods=6))   #从20160502开始生数据
# df['F'] = s1                        #此时F对应的20160501单元格为空
# df2 = df.copy()
# df2[df2>0] = -df2                   #全部数据改为负值
# df1 = df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])   #定义df1,并从df取出前4行，并增加E列（数据为空）
# df1.loc[dates[0]:dates[1],'E'] = 1  #只对E前面两个数进行赋值，后面的赋值
'''
以下两行未显示预期结果，后续再查找原因
df1.dropna(how='any')               #将含有不确定的NaN值所在的整行去掉
df1.fillna(value=1)               #将不确定的NAN值赋值为111
'''
# print pd.isnull(df1)            #以布尔值显示是否存在NAN不确定值
# print df.mean()                 #显示每一列的平均值
# print df.mean(1)                 #显示每一行的平均值
# print s1
# s = pd.Series([1,3,5,np.nan,6,8],index=dates)          #整体下移两位
# print s

df = pd.read_excel('hello.xlsx')    #读取文件
print df.head()