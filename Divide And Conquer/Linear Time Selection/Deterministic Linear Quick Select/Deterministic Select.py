# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:12:18 2020

@author: Ravi
"""

'''
Deterministic Selection Algorithm !(one of the coolest linear time algo)
Running Time O(n) {note that not as practical as randomized, cause the constant here is big compare to randomized}

'''


import random

def partition(x, pivot_index):
    # i = 0
    i = 1
    if pivot_index !=0:
        x[0],x[pivot_index] = x[pivot_index],x[0]
    for j in range(1,len(x)):
        if x[j] < x[0]:
            x[j],x[i] = x[i],x[j]
            i += 1
    x[0],x[i-1] = x[i-1],x[0]
    return i-1

def find_median(arr):
    l = sorted(arr)
    return l[len(l)//2]

def splitter(arr):
    size = 5
    return [ arr[i:(i+size)] for i in range(0,len(arr),size)]

def choose_pivot(arr):
    #if there are only 5 elements return median
    if len(arr)<=5:
        return find_median(arr)
    chunks = splitter(arr)
    sorted_chunks = [sorted(i) for i in chunks]
    medians = [i[len(i)//2] for i in sorted_chunks]
    median_of_medians = choose_pivot(medians)
    return median_of_medians


def Dselect(arr,i):
    if len(arr)==1:
        return arr[0]
    pivot = choose_pivot(arr)
    pivot_index = arr.index(pivot)
    j = partition(arr,pivot_index)
    if j==i:
        return arr[j]
    if i<j:
        return Dselect(arr[:j],i)
    else:
        return Dselect(arr[j+1:],i-j-1)

#use this for testing purpose
# arr = [1,2,3,4,5]
# arr  = random.sample(range(-100,100), 73)
# arr = list(range(0,100))
# print('arr =',arr)
# print('-'*10)
# for i in range(len(arr)):
    # print(Dselect(arr,i),end=" ")
# print(sorted(arr))
# print(Dselect(arr,3))

