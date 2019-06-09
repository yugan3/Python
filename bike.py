# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:31:24 2019

@author: Gan
"""

import numpy as np
import pandas as pd
from datetime import datetime

C = pd.read_csv('C:\\Users\\Gan\\Desktop\\探索美国共享单车数据\\chicago.csv',engine='python')
N = pd.read_csv('C:\\Users\\Gan\\Desktop\\探索美国共享单车数据\\new_york_city.csv',engine='python')
W = pd.read_csv('C:\\Users\\Gan\\Desktop\\探索美国共享单车数据\\washington.csv',engine='python')

# 1.起始时间（Start Time 列）中哪个月份最常见？
# C:6 N:6 W:6
def starttime(x):
    a = list(x['Start Time'].str[5:7])
    a = list(map(int,a)) #将列表中的元素转化为另一种类型元素
    b = [1,2,3,4,5,6,7,8,9,10,11,12]
    c=[]
    for i in b:
        c.append(a.count(i))
    p = c.index(max(c))+1
    return p

# 2.起始时间中，一周的哪一天（比如 Monday, Tuesday）最常见？
# C:Sunday N:Sunday W:Saturday
def day(x):
    a = list(x['Start Time'].str[0:10])
    date = []
    for i in a:
        date.append(datetime.strptime(i,"%Y-%m-%d").weekday())
    date=list(map(lambda x:x+1,date))
    c = [1,2,3,4,5,6,7]
    counts = []
    for j in c:
        counts.append(date.count(j))
    day = c.index(max(c))
    week = {1:'Monday',
            2:'Tuesday',
            3:'Wednesday',
            4:'Thursday',
            5:'Friday',
            6:'Saturday',
            7:'Sunday'
            }
    popdays = week.get(day)
    return popdays

# 3.起始时间中，一天当中哪个小时最常见？
# C:18 N:18 W:9
def hour(x):
    a = list(x['Start Time'].str[11:13])
    a = list(map(int,a))
    hours=[]
    for i in range(25):
        hours.append(a.count(i))
    p = hours.index(max(hours))+1
    return p

# 4.总骑行时长（Trip Duration）是多久，平均骑行时长是多久？
# 总骑行时间： C:280871787 N:269905248 W:371034247
# 平均时间：C:936.23929 N:899.68416 W:1236.7808233333333
def traveltime(x):
    a = list(x['Trip Duration'])
    a = list(map(int,a))
    sum = 0
    for i in a:
        sum = sum + i
    average = sum/300000
    return sum, average

# 5.哪个起始车站（Start Station）最热门，哪个结束车站（End Station）最热门？
#station(C):['Streeter Dr & Grand Ave', 'Streeter Dr & Grand Ave']
#station(N):['Pershing Square North', 'Pershing Square North']
#station(W):['Columbus Circle / Union Station', 'Columbus Circle / Union Station']
def station(x):
    pop=[]
    station = [list(x['Start Station']),list(x['End Station'])]
    for s in station:
        a = list(x['Start Station'])
        b = list(set(a))
        sta = []
        for i in b:
            sta.append(a.count(i))
        index1 = sta.index(max(sta))
        pop.append(b[index1])
    return pop

# 6.哪一趟行程最热门（即，哪一个起始站点与结束站点的组合最热门）？
# C:'Lake Shore Dr & Monroe St/Streeter Dr & Grand Ave' 
# N:'E 7 St & Avenue A/Cooper Square & E 7 St'
# W:'Jefferson Dr & 14th St SW/Jefferson Dr & 14th St SW'
def journey(x):
    x['journey'] =x['Start Station'] +'/'+ x['End Station'] 
    common = x['journey'].value_counts().index[0]
    # value_counts()是pd.Series.value_counts(ascending=False)用法，适用于series
    # -> dataframe也可以使用，默认降序，若需要升序，则ascending=True，取得最小值
    # 这里index(0)直接读取max
    return common

# 7.每种用户类型有多少人？
#city             C             N               W
#Subscriber    238889         269149          220786
#Customer       61110          30159           79214
#Dependent          1
def usertype(x):
    usernumber = x['User Type'].value_counts()
    return usernumber

# 8.每种性别有多少人？
#city         C             N             W      
#Male      181190        204008         NULL
#Female     57758         66783         NULL
def gender(x):
    sex = x['Gender'].value_counts()
    return sex

# 9.出生年份最早的是哪一年、最晚的是哪一年，最常见的是哪一年？
#city               C       N        W
#common          1989    1989     NULL
#max(young)      2016    2001      NULL
#min(old)        1899    1885     NULL
def year(x):
    birth = x['Birth Year'].value_counts().index[0]
    max_birth = max(x['Birth Year'])
    min_birth = min(x['Birth Year'])
    return birth, max_birth, min_birth

        