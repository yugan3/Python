# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:03:38 2019

@author: Gan
"""

a = input()
dic=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in a:
    if i in dic:
        print(i,end="")
        
        
    
a = eval(input())
try:
    if isinstance(a,complex) is True:
        print(a*a)
except:
    print("输入有误")

