# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 6, set 1.2, problem 2
Problem statement: 
    
2) Modify the Graph() class to make a new class called  WeightedGraph() that 
    can implement weighted Graphs.  The WeightedGraph() class should have 
    the following methods    
    
WeightedGraph()	                    creates  a new, empty graph
add_vertex(key)	                    add a vertex to the graph with name "key"
add_edge (vertex1, vertex2, weight)	add an edge from vertex "key1"  to vertex "key2", 
                                    with a certain weight 
find_vertex(key)	                find the vertex named "key" in the graph 
get_vertices()	                    get a list of all vertices
get_edges_and_weights()	            get a list of all edges and their weights
is_adjacent(key1, key2)	            check if key1 and key2 are adjacent, 
                                    returning the weight of their connection if so; return False otherwise    
    
"""


#%% WeightedGraph class
class WeightedGraph:
    """
    Weighted Graph ADT's implementation using a dictionary to store the adjacency list
    """
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, key):
        #every key (vertex) in the dictionary stores a SET of adjancent vertices
        self.graph[key] = set()
        
    def add_edge(self, key1, key2, weight):
        self.graph[key1].add( (key2,weight) )
        self.graph[key2].add( (key1,weight) )
        
    def get_vertices(self):
        for key in self.graph.keys():
            print(key)
   
    def get_edges_and_weights(self):
        for key, edges in self.graph.items():
            print(key, edges)
            
    def is_adjacent(self, key1, key2):
        #loop through all (key,weight) pairs in the first key's adjaceny list entry
        for adjacent in self.graph[key1]:
            #see if you can find the second key in one of the pairs
            #(key is the first value of the pair, the associated weight is the second)
            if adjacent[0] == key2:
                return adjacent[1] #this is the weight
        return False
        
        
    def find_vertex(self,key2find):
        for key in self.graph.keys():
            if (key == key2find):
                print(key, self.graph[key])
                return True
        print("Key not found")
        return False
    
            
#%% testing
wg = WeightedGraph()
wg.add_vertex(4)
wg.add_vertex(5)
wg.add_vertex(11)

wg.get_vertices()
wg.get_edges_and_weights()

wg.add_edge(4,5,50)
wg.add_edge(5,11,100)
wg.get_edges_and_weights()

wg.is_adjacent(4, 5)
wg.is_adjacent(4, 11)

wg.find_vertex(11)
wg.find_vertex(41)