# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 10:29:56 2020

@author: Ravi
"""

prime = [2,3,5,7,11,13,17,19,23,29]
def maximizeProfit(pr,wt,N,W):
    pW=[]
    Wc = 0
    finalLi = []
    for i in range(N):
        pW.append(pr[i]//wt[i])
    for i in range(N):
        x = max(pW)
        ind = pW.index(x)
        if wt[ind]+Wc<=W:
            Wc += wt[ind]     
            finalLi.append(pr[ind])
            pW.remove(x)
    finalLi.sort(reverse = True)
    sum=0
    print(finalLi)
    for i in finalLi:
        if len(prime)>0:
            sum += prime[-1]*i
            print('sum =',str(sum))
            prime.pop()
    return sum

pr = []
wt = []
N, W = map(int,input().split())
for i in range(N):
    x,a = map(int,input().split())
    pr.append(x)
    wt.append(a)
print(maximizeProfit(pr,wt,N,W))
