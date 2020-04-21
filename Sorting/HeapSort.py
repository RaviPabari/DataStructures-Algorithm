# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 02:34:16 2020

@author: Ravi
"""

print("Enter the array :")
arr = list(map(int,input().split()))
def max_heapify(arr,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[l]>arr[largest]:
        largest = l
    else:
        largest = i
    if r<n and arr[r]>arr[largest]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,n,largest)

def build_max_heap(arr):
    i=len(arr)//2
    #here we are starting with n/2 because after n/2 i.e. [ n/2+1 ....n]
    #all the nodes are leaves , and by definition all leaves are maxheaps
    #so there is no need to check them
    n=len(arr)
    while(i>=0):
        max_heapify(arr,n,i)
        i = i-1

def heap_sort(arr):
    build_max_heap(arr) #build the max heap first
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        max_heapify(arr,i,0)
      
