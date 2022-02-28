# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 01:04:25 2021

@author: hp
"""

x = int(input())
l = input()

a = l.count("A")
b = l.count("B")

if a>b:
    print("A")
elif a<b:
    print("B")
else:
    print("Tie")