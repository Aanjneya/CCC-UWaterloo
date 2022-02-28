# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 01:10:19 2021

@author: hp
"""

total = int(input())
total_1 = []
m = int(input())

removed = []

count = total
 
for x in range(1,total+1):
    total_1.append(int(x))
    

for a in range(m):
    y = int(input())
    count = len(total_1)
    #total_1.remove(0)
    #for i in range(0,(count+1),y):
    if 2*y > count:
        total_1.pop(y)
            
    elif 2*y == count:
        total_1.pop(y)
        total_1.pop(2*y)
    else:
        del total_1[1:count+1:y]


print(total_1)  
    
     
