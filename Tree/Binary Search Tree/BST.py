# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:34:30 2020

@author: Ravi
"""

class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
    
    def insert(self,data):
        '''
        Args: Node to be inserted
        
        Now we have to check that the node which was passed has that 
        same data or not because we dont want duplicates
        This is a recursive insert function
        it will check if the value is greater then the parent value
        the it will go left and right accordingly and return True once
        node is created and data is inserted
        '''
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
            
    def height(self):
        lt = -1
        rt = -1
        if self.left:
            lt = self.left.height()
        if self.right:
            rt = self.right.height()
        if lt>rt:
            return lt+1
        else:
            return rt+1
    
    def find(self,data):
        '''
        Args: data to be searched
        If the given data is found then the function returns True
        otherwise returns False
        '''
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    
    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.value)) 
            if self.right:
                self.right.inorder()
    
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))
    
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        '''
        first of all we will check if the root node exists
        if it exists then we will insert the data at the root node
        using the insert fun recursively
        
        Args: data to be inserted
        '''
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
    
    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False
        
    def height(self):
        if not self.root:
            print("height of the tree is 0")
        else:    
            ht = self.root.height()
            print("height of the tree is",str(ht))
    
    def preorder(self):
        print("Preorder Traversal")
        self.root.preorder()
    
    def inorder(self):
        print("Inorder Traversal")
        self.root.inorder()
    
    def postorder(self):
        print("Postorder Traversal")
        self.root.postorder()
    
bst = Tree()
for i in range(5):
    bst.insert(int(input()))
bst.inorder()
bst.postorder()
bst.preorder()   
