"""
An adjacency list is a way of representing a graph as a collection of 
lists. Each vertex in the graph has a list associated with it, which 
contains all the other vertices that are adjacent to it. This representation 
is space-efficient for sparse graphs, where the number of edges is much less 
than the number of vertices squared. It allows efficient traversal of the 
graph, as the neighbors of a vertex can be quickly accessed. Common 
operations like adding a vertex, adding an edge, and querying the neighbors 
of a vertex are efficient. Adjacency lists are commonly used in algorithms 
for graph traversal, such as DFS and BFS.
"""


graph = dict()

graph["A"] = ["A", "B"]
graph["B"] = ["E", "C", "A"]
graph["C"] = ["A", "B", "E", "F"]
graph["E"] = ["C", "F"]
graph["F"] = ["C"]
