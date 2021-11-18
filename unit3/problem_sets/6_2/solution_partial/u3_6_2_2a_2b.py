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
        <YOUR-CODE-HERE>
    
    def set_key(self, key):
        <YOUR-CODE-HERE>

    def get_nxt(self):
        <YOUR-CODE-HERE>
    
    def set_nxt(self, nxt):
        <YOUR-CODE-HERE>

    def get_prv(self):
        <YOUR-CODE-HERE>
    
    def set_prv(self, prv):
        <YOUR-CODE-HERE>


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
        <YOUR-CODE-HERE>
    
    def search_key(self,key):
        <YOUR-CODE-HERE>
    
    def print_all_keys(self):
        <YOUR-CODE-HERE>

    def size(self):
        <YOUR-CODE-HERE>
        
    def delete_key(self, key):
        <YOUR-CODE-HERE>
        
        
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
