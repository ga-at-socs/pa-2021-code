# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 8.2

Problem statement: 
    
3) Implement the Queue ADT using two stacks (you can use the Stack class you create in problem 1). 
You just need to implement the enqueue(Q,x) and dequeue(Q)  operation. What is the time complexity of each operation?

Hint (maybe trying doing this without the hint first though?)

Here's an idea:

Create two stacks, S1 and S2.
Designate S1 as the "queue", with 
the oldest element on top (so dequeue is simply popping S1)
newest element at the bottom, so in order to enqueue an element, you need to empty S1 first, push the new element at the bottom, at then refill S1. 
S2 can be used as the temporary storage for emptying S1 in the previous step
"""
#%% Stack implemented using an array
class Stack_Array:
    """
    The class that implements the Stack ADT using an Array
    """
    def __init__(self,size=0):
        self.arr =  [0]*size
        self.top = -1
        
    def push(self, val):
        self.top += 1
        self.arr[self.top] = val
        
    def pop(self):
        self.top -= 1
        return(self.arr[self.top+1])
    
    def peek(self):
        return(self.arr[self.top])
    
    def stack_size(self):
        return(self.top+1)
        
    def stack_empty(self):
        return(self.top==-1)
        
#%% Queue using two stacks
class Queue:
    """
    The class that implements the Queue ADT using two stacks
    """
    def __init__(self,SIZE):
        self.S1 = Stack_Array(SIZE)
        self.S2 = Stack_Array(SIZE)
        
    def enqueue(self,key):
        #pop elements from S1 to S2 until it is empty
        while(not self.S1.stack_empty()):
            self.S2.push(self.S1.pop())
            
        #now insert new element at the bottom of now-empty S1
        self.S1.push(key)
        
        #pop elements from S2 back into S1
        while(not self.S2.stack_empty()):
            self.S1.push(self.S2.pop())
        
    def dequeue(self):
        return(self.S1.pop())
        

#%% test
q = Queue(100)
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)

q.dequeue()
q.dequeue()
q.dequeue()
