# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:11:48 2021

@author: hp
"""

original = [[1, 2],[3, 4]]

flips = list(input())

for i in range(len(flips)):
    if flips[i] == 'H':
        original[0][0], original[1][0] = original[1][0], original[0][0]
        original[0][1], original[1][1] = original[1][1], original[0][1]
    else:
        original[0][0], original[0][1] = original[0][1], original[0][0]
        original[1][0], original[1][1] = original[1][1], original[1][0]

print(original[0][0], original[0][1])
print(original[1][0], original[1][1])