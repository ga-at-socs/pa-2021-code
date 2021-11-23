# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 6.2

Problem statement: 
    
2a) Create a class NodeDoublyLinkedList which could then be used in the next part to define a DoublyLinkedList class. You should be able to initialize the node with a "key" (or value). The class should have the following methods; the names of the methods are meant to be self-explanatory:

get_key()
set_key()
get_nxt()
set_nxt()
get_prv()
set_prv()

2b) Create a class DoublyLinkedList that can store integers. You can choose to create or omit the tail pointer. It should initialize as an empty list, and the following methods should be defined:

empty()             # checks if linked list is empty
insert_tail()       #inserts a node object of type NodeSinglyLinkedList  at the tail of the list
delete_head()       #delete node at the head of the list, returning its value
search_key()        #search for a given key in the linked list, returns the node if found, None if not found
delete_key()        #delete the node with the given key
size()              #returns the number of nodes in the linked list
print_all_keys()    #iterate through the entire linked list and print all keys

Test all the methods of this linked-list to ensure they work correctly.
"""

#%% Node class
class NodeDoublyLinkedList:
    """
    Doubly linked list node
    """
    def __init__(self,key=0):
        self.key = key
        self.nxt = None
        self.prv = None
        
    def get_key(self):
        return self.key
    
    def set_key(self, key):
        self.key = key

    def get_nxt(self):
        return self.nxt   
    
    def set_nxt(self, nxt):
        self.nxt = nxt

    def get_prv(self):
        return self.prv
    
    def set_prv(self, prv):
        self.prv = prv


#%% DoublyLinkedList class
class DoublyLinkedList:
    """
    Doubly linked list
    Insertion at tail only
    
    """
    def __init__(self):
        self.head = None
        self.tail = None
        
    def empty(self):
        return(self.head == None)

    def insert_tail(self, key):
        #create a new node and set key
        node = NodeDoublyLinkedList(key)

        #node inserted at tail, so its next should point to None
        node.nxt = None
        
        #if the list was empty, then the node is going to be both at the
        #head AND tail, so head needs to updated
        if self.head == None:
            self.head = node
        #if list was not empty, then the tail element's next needs to be updated
        else:
            self.tail.nxt = node
            node.prv = self.tail
        
        #whatever the case may be, the list's tail pointer should point to 
        #this new node
        self.tail = node
        
    def delete_head(self):
        #list is empty, nothing to delete
        if self.head == None:
            return None
        
        #store reference to node to return later
        node = self.head
        
        #list head now points whatever this head node's  nxt pointed to
        self.head = node.nxt
        
        #if this node was the tail node too, then tail pointer needs to point to its prv pointer
        if self.tail == node:
            self.tail = node.prv
        #otherwise, the nodes successor's prv pointer needs to point to where the node's prv pointer is pointing
        else:
            node.nxt.prv = node.prv
    
    def search_key(self,key):
        node = self.head
        while node != None and node.key != key:
            node = node.nxt
        return node   
    
    def print_all_keys(self):
        node = self.head
        while node != None:
            print(f"{node.key},",end="")
            node = node.nxt

    def size(self):
        count = 0
        node = self.head
        while node != None:
            node = node.nxt
            count += 1
        return(count)
        
    def delete_key(self, key):
        #search for the node with this key first
        node = self.search_key(key)
        
        #if not found, return None
        if node == None:
            return None

        #handle the node's next nodes prv pointer
        ##if node is at the tail, then no next node; update tail pointer
        if self.tail == node:
            self.tail = node.prv
        ##otherwise, make the next node's prv point to this node's prv
        else:
            node.nxt.prv = node.prv
        
        #handle the node's previous node's nxt pointer
        ##if this node was at the head, then head pointer needs to be updated
        if self.head == node:
            self.head = node.nxt
        ##otherwise, the previous nodes nxt pointer should point to this node's nxt
        else:
            node.prv.nxt = node.nxt
            
        return node
        
        
#%% Test SinglyLinkedList
# =============================================================================
ll = DoublyLinkedList()
ll.empty()
ll.insert_tail(1)
ll.insert_tail(2)
ll.insert_tail(3)
ll.insert_tail(4)
ll.insert_tail(5)
ll.empty()
ll.print_all_keys()
ll.size()

ll.delete_head()
ll.print_all_keys()
ll.delete_key(4)
ll.print_all_keys()

if ll.search_key(3): print ("Found key")
if ll.search_key(13): print("Found key")
# =============================================================================        
# %%
