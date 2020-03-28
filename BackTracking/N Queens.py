# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 15:38:50 2020

@author: Ravi
"""
'''
One of the most common examples of the backtracking is to arrange N queens on an NxN
chessboard such that no queen can strike down any other queen. A queen can attack
horizontally, vertically, or diagonally. The solution to this problem is also attempted in a
similar way. We first place the first queen anywhere arbitrarily and then place the next queen
in any of the safe places. We continue this process until the number of unplaced queens
becomes zero (a solution is found) or no safe place is left. If no safe place is left, then we
change the position of the previously placed queen.
'''

import time
print("Welcome to the classical N-Queens Problem !\n")
print("Enter the number of Queens you want to place on the board")
N = int(input())
print("\n")
#Initializing the board with 0's
board = [['*']*N for i in range(N)]

def IsUnderAttack(i,j):
    '''
    check if the queen is in row or column
    '''
    for k in range(0,N):
        if board[i][k]=='Q' or board[k][j]=='Q':
            return True
    '''
    check for diagonal atacks 
    '''
    for k in range(0,N):
        for l in range(0,N):
            #for left diagonal ==> row+column
            #for right diagonal ==> row-column
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]=='Q':
                    return True
 
    #if everything is safe then return False
    return False

def SolveNQueen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(IsUnderAttack(i,j))) and (board[i][j]!='Q'):
                board[i][j] = 'Q'
                #recursion
                #wether we can put the next queen with this arrangment or not
                if SolveNQueen(n-1)==True:
                    return True
                board[i][j] = '*'
    return False
start = time.time()
SolveNQueen(N)
end = time.time()
for a in board:
    print(*a)
print("\nRunning time ==>",str(end -start))
