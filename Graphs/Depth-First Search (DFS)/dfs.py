# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:05:54 2020

@author: Ravi
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:40:45 2020

@author: Ravi
"""
'''
works for both directed and undirected graphs
for this testing I have used undirected graph
'''



from collections import deque
#from collections import defaultdict
import time

class Graph:
    def __init__(self,edges):
        self.explored = set()
        self.edges = edges
        self.graph_dict = {}
        self.order = []
        for start,end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)
        # print(self.graph_dict)
        
    def BFS(self,start):
        q = deque()
        self.explored.add(start)
        self.order.append(start)
        q.append(start)
        while len(q)!=0:
            v = q.popleft()
            for edg in self.graph_dict[v]:
                if edg not in self.explored:
                    self.explored.add(edg)
                    self.order.append(edg)
                    q.append(edg)
        # print("exploring order",self.order)
    
    def DFS_recursive(self,start):
        self.explored.add(start)
        self.order.append(start)
        for edg in self.graph_dict[start]:
            if edg not in self.explored:
                self.DFS(edg)
    def DFS_iterative(self,start):
        stack=[]
        self.explored.add(start)
        self.order.append(start)
        stack.append(start)
        while len(stack)!=0:
            v = stack.pop()
            for edg in self.graph_dict[v]:
                if edg not in self.explored:
                    self.explored.add(edg)
                    self.order.append(edg)
                    stack.append(edg)
        print("exploring order BFS :",self.order)
        
    def print(self):
        print('exploring order',self.order)
    
    #incomplete--
    # def get_paths(self,start,end,path=[]):
    #     path = path + [start]
    #     if start == end:
    #         return path
    #     else:
    #         q = deque()
            
            
        

if __name__ == '__main__':

    routes = [
        ("Mumbai","Surat"),
        ("Mumbai","Pune"),
        ("Surat","Mumbai"),
        ("Surat","Banglore"),
        ("Pune","Mumbai"),
        ("Pune","Mysure"),
        ("Pune","Hyderabad"),
        ("Banglore","Mysure"),
        ("Banglore","Hyderabad"),
        ("Banglore","Chennai"),
        ("Hyderabad","Pune"),
        ("Hyderabad","Banglore"),
        ("Hyderabad","Chennai"),
        ("Mysure","Pune"),
        ("Mysure","Banglore"),
        ("Chennai","Hyderabad"),
        ("Chennai","Banglore")
    ]
    start = time.time()
    graph = Graph(routes)
    # print("DFS :")
    # graph.DFS("Mumbai")
    # graph.print()
    # print("---")
    # print("BFS :")
    # graph2 = Graph(routes)
    # graph2.BFS("Mumbai")
    # graph2.print()
    graph.DFS_iterative("Mumbai")
    print("Time =",time.time()-start)