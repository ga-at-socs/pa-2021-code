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
        return self.left        

    def get_right(self):
        return self.right 
    
    def set_key(self,key):
        self.key = key

    def set_left(self,left):
        self.left= left

    def set_right(self,right):
        self.right = right
        
    def set_p(self,p):
        self.p = p 

#%% BST class
class BST:
    """
    The BST class
    """
    
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        inode = Node(key)
        pnode = None
        cnode = self.root

        while cnode != None:
            pnode = cnode
            if inode.key < cnode.key:
                cnode = cnode.left
            else:
                cnode = cnode.right
                
        inode.set_p(pnode)
        
        if pnode == None:
            self.root = inode
        elif inode.key < pnode.key:
            pnode.set_left(inode)
        else:
            pnode.set_right(inode)

    def minimum(self):
        cnode = self.root
        while cnode.left != None:
            cnode = cnode.left
        return (cnode.get_key())
    
    def maximum(self):
        cnode = self.root
        while cnode.right != None:
            cnode = cnode.right
        return (cnode.get_key())    

    def search(self, node, key):
        if node == None or key == node.get_key():
            return node
        
        if key < node.get_key():
            return self.search(node.get_left(), key)
        else:
            return self.search(node.get_right(), key)
                        
    def traverse_in_order(self, node):
        if node != None:
            self.traverse_in_order(node.get_left())
            print (node.get_key())
            self.traverse_in_order(node.get_right())

    def traverse_in_order_2list(self, node, list1):
        if node != None:
            self.traverse_in_order_2list(node.get_left(), list1)
            list1.append(node.get_key())
            self.traverse_in_order_2list(node.get_right(), list1)

            
    def traverse_pre_order(self, node):
        if node != None:
            print (node.get_key())
            self.traverse_pre_order(node.get_left())
            self.traverse_pre_order(node.get_right())

    def traverse_post_order(self, node):
        if node != None:
            self.traverse_post_order(node.get_left())
            self.traverse_post_order(node.get_right())
            print (node.get_key())
 
    def size(self, node):
        if node == None:
            return 0
        else:
            return (self.size(node.get_left()) + self.size(node.get_right()) + 1)

    def height(self, node):
        if node == None:
            return 0
        if node.get_left() == None and node.get_right() == None:
            return 0
        return (max( self.height(node.get_left()), self.height(node.get_right()) ) + 1)

    
    def check_BST(self, node):
        #there is a recursive way to do it, but a simpler way is to simply
        #do an in-order traversal, and then check that it's in ascendign order
        #(in-order traversal of a BST should result in a sorted list)
        #the in-order traversal methods simply prints to screen, which is no good for us
        #so we create another version, traverse_in_order_2list, whih returns a list
        #that results from the in-order traversal
        list1 = []
        bst.traverse_in_order_2list(bst.root, list1)
        return (list1 == sorted(list1))
            
        


#%% Testing insert, min and max
bst = BST()

bst.insert(10)
bst.minimum()
bst.maximum()

bst.insert(7)
bst.minimum()
bst.maximum()

bst.insert(12)
bst.minimum()
bst.maximum()

bst.insert(2)
bst.minimum()
bst.maximum()

bst.insert(16)
bst.minimum()
bst.maximum()

#%% Testing search

sr = bst.search(bst.root, 7)
if (sr):
    print("Found ", sr.get_key())


sr = bst.search(bst.root, 89)
if (sr):
    print("Found ", sr.get_key())

#%% Traversal test
bst.traverse_in_order(bst.root)
bst.traverse_pre_order(bst.root)    
bst.traverse_post_order(bst.root)    

#%% Testing size and height
bst.size(bst.root)
bst.height(bst.root)

#%% check BST condition
bst.check_BST(bst.root)

    

