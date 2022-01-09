# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 12:39:18 2021

@author: admin
"""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def pal(x):
    x1=x[::-1]
    if x==x1:
        print('palindrom')
    else:
        print('not palindrom')
print('i am in mod',__name__)