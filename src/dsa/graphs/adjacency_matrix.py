"""
An adjacency matrix is a way of representing a graph as a 2D array or 
matrix. The rows and columns represent vertices, and the entries in the 
matrix indicate whether an edge exists between pairs of vertices. For an 
unweighted graph, a 1 or 0 in the matrix indicates the presence or absence 
of an edge, respectively. For weighted graphs, the matrix entries can store 
the weights of the edges. This representation is space-efficient for dense 
graphs, where the number of edges is close to the number of vertices 
squared. It allows quick edge existence checks but can be less efficient 
for traversal. Adjacency matrices are useful in algorithms where quick edge 
lookups are required.
"""


graph = dict()

graph["A"] = ["B", "C"]
graph["B"] = ["E", "C", "A"]
graph["C"] = ["A", "B", "E", "F"]
graph["E"] = ["C", "F"]
graph["F"] = ["C"]


matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)


adjacency_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
edges_list = []

for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key, neighbor))

for edge in edges_list:
    first_vertex_index = matrix_elements.index(edge[0])
    second_vertex_index = matrix_elements.index(edge[1])
    adjacency_matrix[first_vertex_index][second_vertex_index] = 1

print(adjacency_matrix)
