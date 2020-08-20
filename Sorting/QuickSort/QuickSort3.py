#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:40:44 2020

@author: ravi
"""

'''
last index is always pivot
'''


from random import randint
import time
count=0
# comparision = 0
def QuickSort(arr,start,end):
    #base condition
    if start<end:
        P = Partition(arr,start,end)
        QuickSort(arr,start,P-1)
        QuickSort(arr,P+1,end)

def Partition(arr,start,end):
    global count
    # pivot_index = randint(start, end)
    # arr[start],arr[pivot_index] = arr[pivot_index],arr[start]
    pivot_index = end
    pivot = arr[end]
    arr[start],arr[pivot_index] = arr[pivot_index],arr[start]
    pivot_index = start
    i = start+1
    for j in range(start+1,end+1):
        if arr[j]<=pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
        count+=1
    arr[pivot_index],arr[i-1] = arr[i-1],arr[pivot_index]
    return i-1

start = time.time()
# arr = [randint(0,100000) for i in range(10)]
path='Quick.txt'
input_list = []
# input_list = [4,5,2,1,9,5,1,1]
with open(path,'r') as f:
    print('Reading from file...')
    for nums in f:
        input_list.append(int(nums))
    print('10,000 numbers loaded...')
QuickSort(input_list,0,len(input_list)-1)
print('Time taken =',time.time()-start)
print('Last index is pivot')
print('number of comparison :',count)
# print(input_list)
