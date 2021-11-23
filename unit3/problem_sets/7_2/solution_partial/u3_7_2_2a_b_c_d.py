# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 7.2

Problem statement: 

2a) Implement the Binary Search Tree (BST) data structure including the 
    following operations: search, min, max, and insert. 
    Use the class structure given in the template file here.
2b) Implement in_order, pre_order and post_order traversals.

2c) Implement a check_BST method that verifies whether a binary tree 
    satisfies the BST property. 
Hint: checking if left node is smaller than the node and right node is 
greater than the node is not enough as the BST constraints apply to the 
whole left and right subtrees. Think recursion.

2d) Implement two more methods, size() and height(), the compute the size 
    (number of nodes) and height (the level of the lowest leaf node(s) 
    in the tree) of the BST.    
    
"""


#%% Node class
class Node:
    """
    Node in a binary tree 
    """
    def __init__(self,key=0):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        
    def get_key(self):
        return self.key
    
    def get_p(self):
        return self.p
    
    def get_left(self):
        <YOUR-CODE-HERE>        

    def get_right(self):
        <YOUR-CODE-HERE>        
    
    def set_key(self,key):
        self.key = key

    def set_left(self,left):
        <YOUR-CODE-HERE>        


    def set_right(self,right):
        <YOUR-CODE-HERE>        
        

#%% BST class
class BST:
    """
    The BST class
    """
    
    def __init__(self):
        self.root = None
        
    def minimum(self):
        <YOUR-CODE-HERE>        

    def maximum(self):
        <YOUR-CODE-HERE>        

    def insert(self, node):
        <YOUR-CODE-HERE>        

    def search(self, node):
        <YOUR-CODE-HERE>        

    def size(self):
        <YOUR-CODE-HERE>        
        
    def height(self):
        <YOUR-CODE-HERE>
        
    def traverse_in_order(self):
        <YOUR-CODE-HERE>                

    def traverse_pre_order(self):
        <YOUR-CODE-HERE>                

    def traverse_post_order(self):
        <YOUR-CODE-HERE>                
                