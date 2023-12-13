# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:07:53 2023

@author: 86176
"""

import pandas as pd
import numpy as np
import random
import re
import matplotlib.pyplot as plt

Read=pd.read_csv("DXYArea (1).csv")
read=Read.groupby(by='countryName').get_group('中国')
#去掉中国，台湾，香港
read=read[read['provinceName']!='中国' ]
read=read[read['provinceName']!='台湾' ]
read=read[read['provinceName']!='香港' ]
#提取年份和月份
read['year']=read['updateTime']
read['month']=read['updateTime']
for i in range(len(read)):
    read.iloc[i,19]=re.findall(r'(\d{4})-',read.iloc[i,19])[0]
    read.iloc[i,20]=re.findall(r'-(\d{2})-',read.iloc[i,20])[0]  
#按省份分组
pname=[]
group=read.groupby(by='provinceName')
yeartotal=[[],[],[]]#2022,2021,2020
yearcure=[[],[],[]]#2022,2021,2020
for name,data in group:
    pname.append(name)
    #每个省份按时间降序排序
    data.sort_values(by="updateTime",ascending=False,inplace=True)
    #按年份分组
    sortyear=data.groupby(by='year')
    i=0
    for year,dat in sortyear:
        temp1=dat.iloc[0,7]
        temp2=dat.iloc[0,9]
        yeartotal[i].append(temp1)
        yearcure[i].append(temp2)
        i=i+1
    #i=0
    #while(i<(len(yeartotal)-1)):
        #yearcha.append(yeartotal[i+1]-yeartotal[i])
#各省每年感染
plt.rcParams['font.family'] = 'KaiTi'

plt.figure(figsize=(32, 14))  # 创建一个32*16英寸的图形对象
plt.plot(pname,yeartotal[0],label='2020')   
plt.plot(pname,yeartotal[1],label='2021')
plt.plot(pname,yeartotal[2],label='2022')
plt.xlabel('省份',fontsize=18)
plt.ylabel('感染人数（人）',fontsize=18)
plt.title('各省感染人数与年份的关系图(折线图)', fontsize=32)
plt.xticks(rotation='vertical') # 横坐标的字竖起来显示
plt.legend()
plt.savefig('infection（折线图）.png')  # 保存为图片文件
plt.show()


#各省每年治愈人数
plt.figure(figsize=(32, 14))  # 创建一个32*16英寸的图形对象
plt.plot(pname,yearcure[0],label='2020')   
plt.plot(pname,yearcure[1],label='2021')
plt.plot(pname,yearcure[2],label='2022')
plt.xlabel('省份',fontsize=18)
plt.ylabel('治愈人数（人）',fontsize=18)
plt.title('各省治愈人数与年份的关系图', fontsize=32)
plt.xticks(rotation='vertical') # 横坐标的字竖起来显示
plt.legend()
plt.savefig('cure.png')  # 保存为图片文件
plt.show()


#感染人数柱状图
ganran=pd.DataFrame({'省份':pname,'2020':yearcure[0],'2021':yearcure[1],'2022':yearcure[2]})
ganran.plot(x='省份',kind='bar',figsize=(32, 14))   
plt.xlabel('省份',fontsize=18)
plt.ylabel('感染人数（人）',fontsize=18)
plt.title('各省感染人数与年份的关系图(柱状图)', fontsize=32)
plt.xticks(rotation='vertical') # 横坐标的字竖起来显示
plt.legend()
plt.savefig('infection(柱状).png')  # 保存为图片文件
plt.show()



#感染人数雷达图
plt.figure(figsize=(32, 14))  # 创建一个32*16英寸的图形对象
DATA={'2020':yeartotal[0],'2021':yeartotal[1],'2022':yeartotal[2]}
DATAlength=len(pname) #数据长度
angles=np.linspace(0,2*np.pi,DATAlength,endpoint=False)
markers='*v^Do'
for col in DATA.keys():
    #使用随机颜色和标记符号
    color='#'+''.join(map('{0:02x}'.format,np.random.randint(0,255,3)))
    plt.polar(angles,DATA[col],color=color,marker=random.choice(markers),label=col)
#设置角度网络标签
plt.thetagrids(angles*180/np.pi,pname,fontproperties='simhei')  
plt.title('各省感染人数与年份雷达图示例', fontsize=32)   
#创建图例
plt.legend()
plt.savefig('infection(雷达图).png')  # 保存为图片文件
plt.show()

#治愈人数雷达图
plt.figure(figsize=(32, 14))  # 创建一个32*16英寸的图形对象
DATA={'2020':yearcure[0],'2021':yearcure[1],'2022':yearcure[2]}
DATAlength=len(pname) #数据长度
angles=np.linspace(0,2*np.pi,DATAlength,endpoint=False)
markers='*v^Do'
for col in DATA.keys():
    #使用随机颜色和标记符号
    color='#'+''.join(map('{0:02x}'.format,np.random.randint(0,255,3)))
    plt.polar(angles,DATA[col],color=color,marker=random.choice(markers),label=col)
#设置角度网络标签
plt.thetagrids(angles*180/np.pi,pname,fontproperties='simhei')  
plt.title('各省治愈人数与年份雷达图示例', fontsize=32)  
#创建图例
plt.legend()
plt.savefig('cure(雷达图).png')  # 保存为图片文件
plt.show()

