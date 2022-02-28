# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:57:04 2021

@author: hp
"""

n = int(input())
intgr, strng = [],[]

for i in range(n):
    xint, xstr = input().split()
    intgr.append(int(xint))
    strng.append(xstr)
    
for z in range(n):
    print (intgr[z]*strng[z])
    

