#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:34:01 2020

@author: ravi
"""
import time
"""
if we can jump 1 or 2 stairs at a time

This is recursive version
"""
def rec_staircase(n):
    if n==0 or n==1:
        return 1
    else:
        return rec_staircase(n-1)+rec_staircase(n-2)
"""
This is bottom up approach or dynamic approach
""" 
def bottom_up_staircase(n):
    a = [0]*(n+1)
    a[0] = 1
    a[1] = 1
    if n==0 or n==1:
        return 1
    else:
        for i in range(2,n+1):
            a[i] = a[i-1]+ a[i-2]
        return a[n]

n=40
start = time.time()
print(bottom_up_staircase(n))
print('time = ',time.time()-start)