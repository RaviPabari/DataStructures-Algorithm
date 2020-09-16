#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:45:18 2020

@author: ravi
"""
import random
import time
#loads the data into dictionary in the form of adjacency list
def load_graph():
    f = open('minCutdata.txt','r')
    adjacency_list = {}
    for line in f:
        temp = list(map(int,line.split()))
        adjacency_list[temp[0]] = temp[1:]
    f.close()
    return adjacency_list

#selects and edge randomly and returns their vertices
def get_random_edges(graph):
    v1 = random.choice(list(graph.keys()))
    v2 = random.choice(list(graph[v1]))
    return v1,v2

#contracts the eges and shrinks 2 vertices into a single vertex
def contract_edge(graph,v1,v2):
    #let s1 and s2 be the neighbours of the vertex v1 and v2
    s1 = graph[v1]
    s2 = graph[v2]
    #now remove self loops causing elements
    s1 = [value for value in s1 if value!=v2]
    s2 = [value for value in s2 if value!=v1]
    #taking union of both neighbours and storing in s1
    s1 = s1+s2
    #overwrite the s1 with the new s1
    graph[v1]=s1
    #delete the second vertex
    del graph[v2]
    #update all the neighbours of all the vertices, so that
    #for further steps no key error occurs
    for vertex in graph:
        for index,neighbour in enumerate(graph[vertex]):
            if neighbour == v2:
                graph[vertex][index] = v1
    #return the updated graph
    return graph
    
def min_cut(graph):
    #run untill only 2 vertices are left
    while len(graph)>2:
        #select an edge randomly
        v1,v2 = get_random_edges(graph)
        #pass the edge(i.e. 2 vertex) to contract into a single vertex
        graph = contract_edge(graph,v1,v2)
    l = list(graph.keys())
    #now count the occurrence of the first vertex in the second vertex
    return graph[l[1]].count(l[0])

#maintain a list of all the min cuts returned by min_cut()
min_list=[]   
#as this algorithm is fast but sometime fails to return the min cut
#so run this for couple of times and return the minimum cut
start = time.time()
for i in range(50):
    #loads the data into graph(dictionary)
    graph = load_graph()
    cut = min_cut(graph)
    min_list.append(cut)
print('--After 50 iterations--')
print("min cut =",min(min_list))
print("time =",time.time()- start)
