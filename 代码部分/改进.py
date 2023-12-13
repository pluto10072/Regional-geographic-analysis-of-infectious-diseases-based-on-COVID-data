# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 13:37:17 2023

@author: 刘浩
"""

import pandas as pd

province = []#省名
#感染总数
total20 = []
total21 = []
total22 = []#2022

year = []#年份
            
file = pd.read_csv('DXYArea .csv')

#单独加一列年份
file['year'] = file['updateTime'].str.extract(r'(20\d{2})-')  

m = 1
n = 1
gro = file.groupby('countryName')#分组
for i in gro:
    if i[0] == '中国': 
        a = i[1].sort_values(by='year',ascending=True)
        gro1 = a.groupby('year')#分组
        for j in gro1:
            year.append(j[0])
            j[1].to_csv(f'{j[0]}.csv')#保存
            gro2 = j[1].groupby('provinceName')#分组
            for k in gro2:
                if m == 1:                    
                    province.append(k[0])
                b = k[1].sort_values(by='updateTime',ascending=False)
                #b.to_csv(f'{k[0]}.csv')#保存
                b = b.reset_index(drop=True)
                if n == 1:                    
                    total20.append(b.loc[0,'province_confirmedCount'])
                elif n == 2:
                    total21.append(b.loc[0,'province_confirmedCount'])
                else:
                    total22.append(b.loc[0,'province_confirmedCount'])
            m = 2    
                    
            n = n + 1        

#三年总数
total = [total20[1],total21[1],total22[1]]

del province[1]#中国
del total20[1]
del total21[1] 
del total22[1]
total1 = list(map(lambda x,y,z:x+y+z,total20,total21,total22))
'''  
del province[4]#台湾
del total[4] 
del province[31]#香港
del total[31]       
del province[1]#中国
del total[1] 
del province[4]#台湾
del total[4] 
del province[31]#香港
del total[31]                                        
'''

import matplotlib.pyplot as plt

#中文设置
plt.rcParams['font.sans-serif'] = 'simhei'
#plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'

#柱状图三年所有
plt.figure(figsize=(18,9))
plt.bar(x = year,
        height = total,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )
plt.xlabel('年份')
plt.ylabel('感染总人数(百万人)')
plt.title("每年感染总人数对比")
plt.show()#展示

#折线图
plt.figure(figsize=(18,9))
plt.plot(
        year,
        total,
        color = 'green',
        #marker='o',
        alpha = 0.4
        )
plt.xlabel('年份')
plt.ylabel('感染总人数(百万人)')
plt.title("每年感染总人数对比")
plt.tight_layout()
plt.show()#展示

#柱状图和折线图组合
fig = plt.figure(figsize=(18,9))
ax1 = fig.add_subplot(111)
ax1.bar(x = year,
        height = total,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )
ax2 = ax1.twinx()
ax2.plot(
        year,
        total,
        color = 'r',
        marker='o',
        alpha = 0.5
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('年份')
plt.ylabel('感染总人数(百万人)')
plt.title("每年感染总人数对比")
plt.show()#展示

#散点图折线图结合
plt.figure(figsize=(18,8))
plt.plot(
        year,
        total,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.scatter(year, total, color = 'r', marker='v', s = 28)
plt.xlabel('年份')
plt.ylabel('感染总人数(百万人)')
plt.title("每年感染总人数对比")
plt.tight_layout()
plt.show()#展示

#----------------------------------------------------------------------
#三年各省所有含香港台湾
#柱状图
plt.figure(figsize=(18,9))
plt.bar(x = province,
        height = total1,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('三年感染总人数(百万人)')
plt.title("三年各省感染总人数对比(含香港台湾)")
plt.show()#展示

#折线图
plt.figure(figsize=(18,9))
plt.plot(
        province,
        total1,
        color = 'green',
        #marker='o',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('三年感染总人数(百万人)')
plt.title("三年各省感染总人数对比(含香港台湾)")
plt.tight_layout()
plt.show()#展示

#柱状图和折线图组合
fig = plt.figure(figsize=(18,9))
ax1 = fig.add_subplot(111)
ax1.bar(x = province,
        height = total1,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
ax2 = ax1.twinx()
ax2.plot(
        province,
        total1,
        color = 'r',
        marker='o',
        alpha = 0.5
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('三年感染总人数(百万人)')
plt.title("三年各省感染总人数对比(含香港台湾)")
plt.show()#展示

#散点图
plt.figure(figsize=(18,8))
plt.plot(
        province,
        total1,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.scatter(province, total1, color = 'r', marker='v', s = 28)
plt.xlabel('省份')
plt.ylabel('三年感染总人数(百万人)')
plt.title("三年各省感染总人数对比(含香港台湾)")
plt.tight_layout()
plt.show()#展示

#----------------------------------------------------------------------
del province[4]#台湾
del total1[4] 
del province[31]#香港
del total1[31]       
#三年各省所有不含香港台湾
#柱状图
plt.figure(figsize=(18,9))
plt.bar(x = province,
        height = total1,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('三年感染总人数(人)')
plt.title("三年各省感染总人数对比(不含香港台湾)")
plt.show()#展示

#折线图
plt.figure(figsize=(18,9))
plt.plot(
        province,
        total1,
        color = 'green',
        #marker='o',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('三年感染总人数(人)')
plt.title("三年各省感染总人数对比(不含香港台湾)")
plt.tight_layout()
plt.show()#展示

#柱状图和折线图组合
fig = plt.figure(figsize=(18,9))
ax1 = fig.add_subplot(111)
ax1.bar(x = province,
        height = total1,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
ax2 = ax1.twinx()
ax2.plot(
        province,
        total1,
        color = 'r',
        marker='o',
        alpha = 0.5
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('三年感染总人数(人)')
plt.title("三年各省感染总人数对比(不含香港台湾)")
plt.show()#展示

#散点图
plt.figure(figsize=(18,8))
plt.plot(
        province,
        total1,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.scatter(province, total1, color = 'r', marker='v', s = 28)
plt.xlabel('省份')
plt.ylabel('三年感染总人数(人)')
plt.title("三年各省感染总人数对比(不含香港台湾)")
plt.tight_layout()
plt.show()#展示


#----------------------------------------------------------------------
#各年各省不含香港台湾
#台湾
del total20[4] 
del total21[4]
del total22[4]
#香港
del total20[31]   
del total21[31]
del total22[31]
#柱状图
plt.figure(figsize=(18,9))
plt.bar(x = province,
        height = total20,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2020年感染总人数(人)')
plt.title("三2020各省感染总人数对比(不含香港台湾)")
plt.show()#展示

#折线图
plt.figure(figsize=(18,9))
plt.plot(
        province,
        total20,
        color = 'green',
        #marker='o',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2020年感染总人数(人)')
plt.title("2020年各省感染总人数对比(不含香港台湾)")
plt.tight_layout()
plt.show()#展示

#柱状图和折线图组合
fig = plt.figure(figsize=(18,9))
ax1 = fig.add_subplot(111)
ax1.bar(x = province,
        height = total20,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
ax2 = ax1.twinx()
ax2.plot(
        province,
        total20,
        color = 'r',
        marker='o',
        alpha = 0.5
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2020年感染总人数(人)')
plt.title("2020年各省感染总人数对比(不含香港台湾)")
plt.show()#展示

#散点图
plt.figure(figsize=(18,8))
plt.plot(
        province,
        total20,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.scatter(province, total20, color = 'r', marker='v', s = 28)
plt.xlabel('省份')
plt.ylabel('2020年感染总人数(人)')
plt.title("2020年各省感染总人数对比(不含香港台湾)")
plt.tight_layout()
plt.show()#展示

#----------------
#柱状图
plt.figure(figsize=(18,9))
plt.bar(x = province,
        height = total21,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2021年感染总人数(人)')
plt.title("三2021各省感染总人数对比(不含香港台湾)")
plt.show()#展示

#折线图
plt.figure(figsize=(18,9))
plt.plot(
        province,
        total21,
        color = 'green',
        #marker='o',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2021年感染总人数(人)')
plt.title("2021年各省感染总人数对比(不含香港台湾)")
plt.tight_layout()
plt.show()#展示

#柱状图和折线图组合
fig = plt.figure(figsize=(18,9))
ax1 = fig.add_subplot(111)
ax1.bar(x = province,
        height = total21,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
ax2 = ax1.twinx()
ax2.plot(
        province,
        total21,
        color = 'r',
        marker='o',
        alpha = 0.5
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2021年感染总人数(人)')
plt.title("2021年各省感染总人数对比(不含香港台湾)")
plt.show()#展示

#散点图
plt.figure(figsize=(18,8))
plt.plot(
        province,
        total21,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.scatter(province, total21, color = 'r', marker='v', s = 28)
plt.xlabel('省份')
plt.ylabel('2021年感染总人数(人)')
plt.title("2021年各省感染总人数对比(不含香港台湾)")
plt.tight_layout()
plt.show()#展示

#----------
#柱状图
plt.figure(figsize=(18,9))
plt.bar(x = province,
        height = total22,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2022年感染总人数(人)')
plt.title("2022年各省感染总人数对比(不含香港台湾)")
plt.show()#展示

#折线图
plt.figure(figsize=(18,9))
plt.plot(
        province,
        total22,
        color = 'green',
        #marker='o',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2022年感染总人数(人)')
plt.title("2022年各省感染总人数对比(不含香港台湾)")
plt.tight_layout()
plt.show()#展示

#柱状图和折线图组合
fig = plt.figure(figsize=(18,9))
ax1 = fig.add_subplot(111)
ax1.bar(x = province,
        height = total22,
        width= 0.5,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
ax2 = ax1.twinx()
ax2.plot(
        province,
        total22,
        color = 'r',
        marker='o',
        alpha = 0.5
        )#省名为横坐标，感各省染总数为纵坐标
plt.xlabel('省份')
plt.ylabel('2022年感染总人数(人)')
plt.title("2022年各省感染总人数对比(不含香港台湾)")
plt.show()#展示

#散点图
plt.figure(figsize=(18,8))
plt.plot(
        province,
        total22,
        color = 'green',
        alpha = 0.4
        )#省名为横坐标，感各省染总数为纵坐标
plt.scatter(province, total22, color = 'r', marker='v', s = 28)
plt.xlabel('省份')
plt.ylabel('2022年感染总人数(人)')
plt.title("2022年各省感染总人数对比(不含香港台湾)")
plt.tight_layout()
plt.show()#展示