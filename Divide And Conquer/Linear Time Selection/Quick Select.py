# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:53:34 2020

@author: Ravi
"""

'''
Random Selection Algorithm to compute ith order statistic in O(n) time with 
high probability, this algorithm is just a made by simple modification of 
Quick Sort. If we are very very unlucky then worst case running time = O(n**2) 

This problem can be solved with the help of sorting which will take
Omega(nlogn).
'''

from random import randrange

def partition(arr,pivot_index = 0):
    ''' 
   Parameters
    ----------
    arr : array which have to be partitioned
    pivot_index : random index from {0,len(arr)}
    
    Returns
    -------
    i   : index around which the array is partitioned
    arr : partitioned array.

    '''
    #swap the first and the pivot index for simplification
    if pivot_index!=0:
        arr[0],arr[pivot_index] = arr[pivot_index],arr[0]
    #make the pivot index 0 and the content of that index into pivot
    pivot_index = 0
    pivot = arr[0]
    #initialize both pointers i and j with 1
    i=1
    #loop until the last element
    for j in range(1,len(arr)):
        #swap if lower element is found
        if arr[j]<=pivot and j!= pivot_index :
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    #swap the pivot with the i-1 (we are taking i-1 because we have inititalize
    # i with 1 that is one index after the pivot from the original )
    arr[pivot_index],arr[i-1] = arr[i-1],arr[pivot_index]
    #return both the partitioned array
    #And the pivot index which is at its sorted position
    return i-1,arr


def Rselect(arr,i):
    '''
    Rselect call itself for finding the index we are looking for
    
    Parameters
    ----------
    arr : input array  
    i : the ith order statistics we want to find

    Returns
    -------
    i : The ith order statistic index which we are looking for 

    '''
    #base condition if length is 1 return that element
    if len(arr)==1:
        return arr[0]
    #partition the array around the pivot
    j,arr = partition(arr,randrange(len(arr)))
    #if the pivot index is same as we are looking for return it simply
    if i==j:
        return arr[j]
    #if the pivot index is greater than we only have to 
    #recurse on the left sub array
    if i<j:
        return Rselect(arr[:j],i)
    #if the pivot index if lessert than we only have to
    #recurse on the right sub array
    else:
        return Rselect(arr[j+1:],i-j-1)

arr = [1,2,3,4,4,4,4,5,6,7,8]
for i in range(len(arr)):
    print(Rselect(arr, i))
