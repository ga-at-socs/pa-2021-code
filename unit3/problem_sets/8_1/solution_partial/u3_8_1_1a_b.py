# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 3, set 8.1

Problem statement: 

1) Stack ADT

1a) Create a class "Stack" the implements the Stack Abstract Data Type using 
    an Array. You should be able to initialize the Stack with a certain 
    maximum size. The Stack class should implement the following functions:

push(S,x)    #insert element x in stack S
pop(S)       #remove and return the most recently inserted element from stack S
peek(S)      #return (but don’t remove) the most recently inserted element from stack S
stack_size(S)#return the number of elements stored in stack S
stack_empty(S) #test if stack S is empty
You should check for underflow, but overflow detection is optional.2) 

1b)  Using your Stack implementation from 1a, write a program that simulates 
    the "go back" operation of a web browser. 
    The behaviour of this application should be as follows:

When the program is run, the user should be shown this prompt: 
"You are on your home page. Enter the url you wish to visit next (or "q" to quit).
The user should be able to enter any url at this point. 
You don't need to check if url's are in the correct format. 
Any string input should just be accepted.
Other than when you are at the home page (where there is no back option), 
every time a user enters a url, you should display this message:
"You are currently visiting the webpage at this url:<the-current-url>.
Enter the url you wish to visit next (or "q" to quit, "b" to go back to previous url).

Hint: "Push" every new URL visited into your stack. 
When the user presses "b", simply pop the stack and display the result.   
    
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
        <YOUR-CODE-HERE>
    
    def peek(self):
        <YOUR-CODE-HERE>
    
    def stack_size(self):
        <YOUR-CODE-HERE>
        
    def stack_empty(self):
        <YOUR-CODE-HERE>
        

#%% Test it
"""        
sa = Stack_Array(10)
sa.stack_empty()
sa.stack_size()
sa.push("test")
sa.push("this")
sa.stack_empty()
sa.stack_size()
sa.pop()
sa.pop()
sa.stack_empty()
sa.stack_size()
"""
        
#%% 1b: The "web browser"

# initialize the stack, insert home page as the first page visited
url_stack = Stack_Array(100)
home = "home.html"
current_url = home

#the first prompt outside the loop
url = input("You are on your home page. Enter the url you wish to visit next (or \"q\" to quit) : ")
    
while(True):
     <YOUR-CODE-HERE>
