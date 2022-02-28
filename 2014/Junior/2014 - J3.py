# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 00:45:10 2021

@author: hp
"""
times = int(input())

a, d =[],[]

counta = 100
countd = 100

for i in range(times):
    ap,dp = input().split(" ")
    a.append(int(ap))
    d.append(int(dp))
    if int(a[i]) > int(d[i]):
        countd -= int(a[i])
        counta = counta
    elif int(a[i]) < int(d[i]):
        countd = countd
        counta -= int(d[i])
    elif int(a[i]) < int(d[i]):
        counta = counta
        countd = countd
    
print (counta)
print (countd)