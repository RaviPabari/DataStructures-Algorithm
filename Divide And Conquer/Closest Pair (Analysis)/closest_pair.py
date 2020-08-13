# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Tue Aug 12 22:37:02 2020
@author: Ravi
"""
import time
from math import sqrt
import testcases

def eucl_dist(a,b):
    '''
    input  : tuples containing x-cord and y-cord 
    return : distance(int)
    '''
    x1,y1 = a[0],a[1]
    x2,y2 = b[0],b[1]
    return (sqrt((x1-x2)**2 + (y1-y2)**2))

def brute_force(points):
    '''
    input  : list of points with len <= 3
    return : 2 points with minimum distance
    '''
    p1 = points[0]
    p2 = points[1]
    min_dist = eucl_dist(p1,p2)
    l = len(points)
    for i in range(l-1):
        for j in range(i+1,l):
            min_dist2 = eucl_dist(points[i],points[j])
            if min_dist2 < min_dist:
                min_dist = min_dist2
                p1,p2 = points[i],points[j]
    return (p1,p2,min_dist)

def closest_pair(points,p1,p2,dist):
    '''
    input  :list of points and initial points p1 and p2 along their distance value for comparing
    return :2 points with minimum distance
    '''
    l = len(points)
    if l<=3:
        return brute_force(points)
    #divide and conquer now
    mid = l//2
    mid_x = points[mid][0] #extracting the middle x co-ordinate of the middle point in the plane
    #left and right sub array
    L = points[:mid]
    R = points[mid:]
    #now just recurse on left and right sub array with
    #searching points and updating them along distances in left side, right side and finally at strip
    p1,p2,min_dist = closest_pair(L,p1,p2,dist)#left
    p1,p2,min_dist = closest_pair(R,p1,p2,min_dist)#Right
    p1,p2,min_dist = split_pair(points,mid_x,p1,p2,min_dist)#split

    return (p1,p2,min_dist)

def split_pair(points,x_cord,p1,p2,min_dist):
    '''
    input  : list of points and x-cordinate with current 2 points with their min dist
    return : 2 points with minimum distance
    '''
    #initialize empty list to store all the points which are around the split line or middle line
    split = []
    #so points should not be beyond right and left side of the split line
    right , left = x_cord+dist, x_cord-dist
    #store all the points that are in that region
    #    .  |
    #   .   |  (right boundary)
    #.      |------->
    #       |   .
    #(left) |      .
    #<------| .
    #    .  |       .
    #   .   |
    #so all that points which are between the < left - middle - right > are added to the split list 
    for i in points:
        if i[0]<left or i[0]>right: break
        elif left <= i[0] <= right: split.append(i)
    #sorting the spit list according to y-cord
    split.sort(key=lambda x:x[1])
    #now just simply bruteforce
    for i in range(len(split)-1):
        for j in range(i+1,len(split)):
            distance = eucl_dist(split[i],split[j])
            if distance<min_dist:
                min_dist = distance
                p1,p2 = split[i],split[j]
    return p1,p2,min_dist


print('*'*10)
start = time.time()
points = testcases.points1
points.sort()
p1,p2 = points[0],points[1]
dist = eucl_dist(p1,p2)
P1,P2,Min_dist = closest_pair(points, p1, p2, dist)
print('Length of the 1st testcase =',len(points))
print('1st Point',P1)
print('2nd Point',P2)
print('Distance',Min_dist)
print('Time taken =',time.time()-start)
print('*'*10)
start = time.time()
points = testcases.points2
points.sort()
p1,p2 = points[0],points[1]
dist = eucl_dist(p1,p2)
P1,P2,Min_dist = closest_pair(points, p1, p2, dist)
print('Length of the 2nd testcase =',len(points))
print('1st Point',P1)
print('2nd Point',P2)
print('Distance',Min_dist)
print('Time taken =',time.time()-start)
print('*'*10)
start = time.time()
points = testcases.points3
points.sort()
p1,p2 = points[0],points[1]
dist = eucl_dist(p1,p2)
P1,P2,Min_dist = closest_pair(points, p1, p2, dist)
print('Length of the 3rd testcase =',len(points))
print('1st Point',P1)
print('2nd Point',P2)
print('Distance',Min_dist)
print('Time taken =',time.time()-start)
print('*'*10)
start = time.time()
points = testcases.points4
points.sort()
p1,p2 = points[0],points[1]
dist = eucl_dist(p1,p2)
P1,P2,Min_dist = closest_pair(points, p1, p2, dist)
print('Length of the 4th testcase =',len(points))
print('1st Point',P1)
print('2nd Point',P2)
print('Distance',Min_dist)
print('Time taken =',time.time()-start)
print('*'*10)
start = time.time()
points = testcases.points5
points.sort()
p1,p2 = points[0],points[1]
dist = eucl_dist(p1,p2)
P1,P2,Min_dist = closest_pair(points, p1, p2, dist)
print('Length of the 5th testcase =',len(points))
print('1st Point',P1)
print('2nd Point',P2)
print('Distance',Min_dist)
print('Time taken =',time.time()-start)
print('*'*10)
