# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 6, set 1.2, problem 1
Problem statement: 
    
1) Create a class Graph() that implements a graph ADT. It should use a 
    dictionary internally to store the graph, and implement all the ADT 
    functions described here:
        
Graph()	                creates  a new, empty graph
add_vertex(key)	        add a vertex to the graph with name "key"
add_edge (key1, key2)	add an edge from vertex "key1"  to vertex "key2"
find_vertex(key)        find the vertex named "key" in the graph 
get_vertices()	        get a list of all vertices
get_edges()	            get a list of all edges
is_adjacent(key1, key2)	checks if two given vertices are adjacent       
        
"""


#%% Graph class
class Graph:
    """
    Graph ADT's implementation using a dictionary to store the adjacency list
    """
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, key):
        #every key (vertex) in the dictionary stores a SET of adjancent vertices
        self.graph[key] = set()
        
    def add_edge<YOUR-CODE-HERE>         

        
    def get_vertices<YOUR-CODE-HERE>         

   
    def get_edges<YOUR-CODE-HERE>         

            
    def is_adjacent<YOUR-CODE-HERE>         

    
    def find_vertex(self,key2find):
<YOUR-CODE-HERE>         
        print("Key not found")
        return False
    
            
#%% testing
g = Graph()
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(11)

g.get_vertices()
g.get_edges()

g.add_edge(4,5)
g.add_edge(5,11)
g.get_edges()

g.is_adjacent(4, 5)
g.is_adjacent(4, 11)

g.find_vertex(11)
g.find_vertex(41)