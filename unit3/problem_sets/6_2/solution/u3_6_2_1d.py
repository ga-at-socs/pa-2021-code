# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 6.2

Problem statement: 
    
1d) Modify 1b to add a *tail pointer* to the linked-list data structure. Now add an insert_tail() method to it.
    
Where:    

1a) Create a class NodeSinglyLinkedList* which could then be used in the next part to define a SinglyLinkedList class. You should be able to initialize the node with a "key" (or value). The class should have the following methods; the names of the methods are meant to be self-explanatory:
get_key()
set_key()
get_next()
set_next()

1b) Create a class SinglyLinkedList that can store integers. For this part, it should have a head pointer only (so no tail pointer). It should initialize as an empty list, and the following methods should be defined:

empty()          # checks if linked list is empty
insert_head()    #inserts a node object of type NodeSinglyLinkedList at the head of the list
search_key()     #search for a given key in the linked list, returns the node if found, None if not found
size()           #returns the number of nodes in the linked list
print_all_keys() #iterate through the entire linked list and print all keys


Test all the methods of this linked-list to ensure they work correctly.
"""

#%% Node class
class NodeSinglyLinkedList:
    """
    Singly linked list node
    """
    def __init__(self,key=0):
        self.key = key
        self.nxt = None
        
    def get_key(self):
        return self.key
    
    def set_key(self,key):
        self.key = key

    def get_nxt(self):
        return self.nxt   
    
    def set_nxt(self,nxt):
        self.nxt = nxt

#%% SinglyLinkedList class
class SinglyLinkedList:
    """
    Singly linked list, with head AND tail pointer only
    Insertion at the head and tail both
    """
    def __init__(self):
        self.head = None
        self.tail = None
        
    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def insert_head(self, key):
        #create a new node and set key
        node = NodeSinglyLinkedList(key)

        #node inserted at head, so its next should point to where the list head was pointing
        node.nxt = self.head

        #the list's head should now be updatd to point at this new node
        self.head = node
        
        #since we have a tail pointer, it needs to be updated if the list 
        #was empty to begin with
        if self.tail == None:
            self.tail = node

    def insert_tail(self, key):
        #create a new node and set key
        node = NodeSinglyLinkedList(key)

        #node inserted at tail, so its next should point to None
        node.nxt = None
        
        #if the list was empty, then the node is going to be both at the
        #head AND tail, so head needs to updated
        if self.head == None:
            self.head = node
        #if list was not empty, then the tail element's next needs to be updated
        else:
            self.tail.nxt = node
        
        #whatever the case may be, the list's tail pointer should point to 
        #this new node
        self.tail = node
        
    def search_key(self,key):
        node = self.head
        while node != None and node.key != key:
            node = node.nxt
        return node    

    def size(self):
        count = 0
        node = self.head
        while node != None:
            node = node.nxt
            count += 1
        return(count)

        
    def print_all_keys(self):
        node = self.head
        while node != None:
            print(f"{node.key},",end="")
            node = node.nxt

#%% Test SinglyLinkedList
# =============================================================================
ll = SinglyLinkedList()
ll.empty()
ll.insert_tail(1)
ll.insert_tail(2)
ll.insert_tail(3)
ll.insert_tail(4)
ll.empty()
ll.print_all_keys()
ll.size()
if ll.search_key(3): print ("Found key")
if ll.search_key(13): print("Found key")
# =============================================================================        
# %%
