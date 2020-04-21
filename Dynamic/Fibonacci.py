# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:53:58 2020

@author: Ravi
"""
# O(n) and Space(n)
def fibo(n):
    fib = [0]*(n+1)
    fib[0]=0
    fib[1]=1
    for i in range(2,n+1):
        fib[i] = fib[i-1]+fib[i-2]
    print(fib[n])

# O(n) and Space(1)
def fibo2(n):
    a = 0
    b = 1
    if n<=1:
        return n
    else:
        for i in range(2,n+1):
            a,b = b,a+b
        return b
        
n = int(input())
#fibo(n)
#print(fibo2(n))
