# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:44:16 2020

@author: Ravi
"""
#Topological Sorting using recursive DFS
# {1: [3], 2: [3], 4: [0, 1], 5: [0, 2]}
# topological order = [3,1,2,1,0,4,5]
# 1->3
# 2->3
# 4->0->1
class Graph:
    def __init__(self,edges):
        self.explored = set()
        self.edges = edges
        self.graph_dict = {1: [2],
                             2: [3, 4],
                             3: [11, 8],
                             4: [5, 7],
                             5: [6],
                             6: [7],
                             7: [5],
                             8: [7, 9, 10],
                             9: [6, 10],
                             10: [11],
                             11: [8]}# {1: [3], 2: [3], 4: [0, 1], 5: [0, 2]}
        self.order = []
        # for start,end in self.edges:
        #     if start not in self.graph_dict:
        #         self.graph_dict[start] = [end]
        #     else:
        #         self.graph_dict[start].append(end)
        # print(self.graph_dict)
        self.nodes = list(self.graph_dict.keys())
        
    def topological_ordering(self):
        for i in self.nodes:
            if i not in self.explored:
                self.order.append(i)
            self.dfs_helper(i)
        
    def dfs_helper(self,start):
        if start not in self.explored:
            self.explored.add(start)
            if start in self.graph_dict:
                for edg in self.graph_dict[start]:
                    if edg not in self.explored:
                        self.order.append(edg) #this sould be commented out for reverse
                        self.dfs_helper(edg)
            # self.order.append(start) {computes reverse topsort}

        
    def print(self):
        print(self.order)

if __name__ == '__main__':
    routes =[
        (5, 2),
        (5, 0),
        (4, 0), 
        (4, 1),
        (2, 3), 
        (3, 1)
        # (1,None)
    ]
    routes2 = [
        ('a','c'),
        ('a','b'),
        ('b','e'),
        ('c','e'),
        ('c','d'),
        ('d','f'),
        ('e','f')
    ]
    graph = Graph(routes)
    graph.topological_ordering()
    graph.print()
    # graph.Topological_ordering()  
