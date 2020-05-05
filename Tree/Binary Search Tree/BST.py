# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:48:09 2020

@author: Ravi
"""
"""
This is an augmented Binary Search Tree with Height Augmentation, and has track of parent nodes
Every node has its height/depth and it's parent node info with it so computing height when needed
becomes O(1) which will be helpful for building Balanced Binary Tree (AVL Tree)
"""
def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = 1+max(height(node.left),height(node.right))

class Node:
    """Creates a node.
        
        Args:
            parent: The node's parent.
    """
    def __init__(self,val,parent):
        self.value = val
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0
    
    def _insert(self,node):
        """Inserts a node into the subtree rooted at this node.
        
        Args:
            node: The node to be inserted.
        """
        if node is None:
            return
        if node.value == self.value:
            return
        if node.value < self.value:
            if self.left:
                self.left._insert(node)
            else:
                node.parent = self
                self.left = node
        else:
            if self.right:
                self.right._insert(node)
            else:
                node.parent = self
                self.right = node
        update_height(self)
    
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.inorder()
                
    def preorder(self):
        if self:
            print(self.value)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.value)
                
    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.value)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width
    
    def __str__(self):
        return '\n'.join(self._str()[0])
    
    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted at this 
        node.
        
        Returns:
            The node with the minimum key.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def find_max(self):
        """Finds the node with the maximum key in the subtree rooted at this 
        node.
        
        Returns:
            The node with the maximum key.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current
    
    def next_smaller(self):
        """
         Returns the node with the next larger key (the successor) in the BST.
        """
        #case 1 if left sub tree exists
        if self.left:
            return self.left.find_max()
        #case 2 if no left subtree
        current = self
        while current.parent and current is current.parent:
            current = current.parent
        return current
    
    def next_larger(self):
        """Returns the node with the next smaller key (the predecessor) in the BST.
        """
        #case 1 if right subtree exists
        if self.right:
            return self.right.find_min()
        #case 2 if no right subtee
        current = self
        while current.parent and current is current.parent.right:
            current = current.parent
        return current.parent
    
    def _height(self):
        """ return the self.height of the tree"""
        return self.height
    
    def find(self,data):
        """Finds and returns the node with key k from the subtree rooted at this 
        node.
        
        Args:
            data: The key of the node we want to find.
        
        Returns:
            The node with key data.
        """
        if self.value == data:
            return self
        
        if self.value > data:
            if self.left:
                return self.left.find(data)
        else:
            if self.right:
                return self.right.find(data)
        return None
    
    def delete(self):
       """Deletes and returns this node from the BST."""
       if self.left is None or self.right is None:
           if self is self.parent.left:
               self.parent.left = self.left or self.right
               if self.parent.left is not None:
                   self.parent.left.parent = self.parent
           else:
               self.parent.right = self.left or self.right
               if self.parent.right is not None:
                   self.parent.right.parent = self.parent
       else:
           s = self.next_larger()
           self.value,s.value = s.value,self.value
           return s.delete()
                  
class BST(object):
    """A binary search tree."""
     
    def __init__(self):
        """Creates an empty BST."""
        self.root = None
    
    def insert(self,data):
        """Inserts a node with key data into the subtree rooted at this node.
        
        Args:
            k: The key of the node to be inserted.
            
        Returns:
            The node inserted.
        """
        node = Node(data,None)
        if self.root is None:
            self.root = node
        else:
            self.root._insert(node)
    
    def inorder(self):
        print("Inorder Traversal")
        self.root.inorder()
    
    def preorder(self):
        print("Preorder Traversal")
        self.root.preorder()
    
    def postorder(self):
        print("Postorder Traversal")
        self.root.postorder()
    
    def __str__(self):
        if self.root is None: return '<empty tree>'
        return str(self.root)
    
    def find_min(self):
        """Returns the minimum node of this BST."""
        if self.root:
            return self.root.find_min()
    
    def find_max(self):
        """Returns the maximum node of this BST."""
        if self.root:
            return self.root.find_max()
    
    def next_larger(self):
        """Returns the node that contains the next larger (the successor) key in
        the BST in relation to the node.
        
        Args:
            data: The key of the node of which the successor is to be found.
            
        Returns:
            The successor node.
        """
        if self.root:
            return self.root.next_larger()
    
    def next_smaller(self):
        if self.root:
            return self.root.next_smaller()
    
    def height(self):
        """ Return the height of the tree"""
        if self.root:
            return self.root._height()
        
    def help(self):
        print("-----------------------\n")
        print(":: Available functions you can use on BST::\n")
        helper = ['insert','delete','print(tree)','inorder','preorder','postorder',
                  'find_min','find(key)','find_max','next_larger','next_smaller','height']
        for i in range(len(helper)):
            print("--->  ."+helper[i])
        print("\n-----------------------")
    
    def find(self,data):
        """Finds and returns the node with key k from the subtree rooted at this 
        node.
        
        Args:
            k: The key of the node we want to find.
        
        Returns:
            The node with key k or None if the tree is empty.
        """
        if self.root:
            return self.root.find(data)
    
    def delete(self,data):
        """Deletes and returns a node with key k if it exists from the BST.
        
        Args:
            k: The key of the node that we want to delete.
            
        Returns:
            The deleted node with key data.
        """
        node = self.root.find(data)
        if node:
            if node is self.root:
                pseudoroot = Node(0,None)
                pseudoroot.left = self.root
                self.root.parent = pseudoroot
                deleted = self.root.delete()
                self.root = pseudoroot.left
                if self.root is not None:
                    self.root.parent = None
                return deleted
            else:
                return node.delete()
        
#Testing#
#import random
#arr = []
#for i in range(8):
#    arr.append(random.randint(1,1000))
#bst = BST()
#bst.insert(436)
#bst.insert(49)
#bst.insert(136)
#bst.insert(439)
#bst.insert(134)
#bst.insert(47)
#bst.insert(184)
#bst.insert(136)
#bst.insert(503)
#bst.insert(437)
#bst.insert(480)
#for i in range(len(arr)):
#    bst.insert(arr[i])
#bst.preorder()
#bst.delete(439)
#print(bst)
#bst.help()
#print(bst.find(85))   
#bst.find_min()
#bst.next_larger()
#bst.next_smaller()
#print(bst.height())
