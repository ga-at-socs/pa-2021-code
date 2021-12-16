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
        
<YOUR-CODE-HERE>    
            
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