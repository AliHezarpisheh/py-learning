"""
Breadth-First Search (BFS) is a graph traversal algorithm that explores 
the neighbor nodes at the present depth prior to moving on to nodes at the 
next depth level. Starting from a source node, it visits all nodes at the 
present depth level before moving on to the nodes at the next depth level. 
This approach can be implemented using a queue data structure. BFS is 
useful for finding the shortest path in unweighted graphs, as well as in 
solving problems like finding connected components and level-order traversal 
in trees. Its time complexity is O(V + E), where V is the number of vertices 
and E is the number of edges.
"""

from collections import deque

graph = dict()
graph["A"] = ["B", "G", "D"]
graph["B"] = ["A", "F", "E"]
graph["C"] = ["F", "H"]
graph["D"] = ["F", "A"]
graph["E"] = ["B", "G"]
graph["F"] = ["B", "D", "C"]
graph["G"] = ["A", "E"]
graph["H"] = ["C"]


def breadth_first_traversal(graph: dict[str, list[str]], root: str) -> list[str]:
    """
    Perform breadth-first traversal on a graph.

    Parameters
    ----------
    graph : dict[str, list[str]]
        The graph represented as an adjacency list.
    root : str
        The starting vertex for the traversal.

    Returns
    -------
    list[str]
        The list of vertices visited in breadth-first order.
    """
    visited_vertices = []
    graph_queue = deque([root])

    visited_vertices.append(root)
    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]

        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elm in sorted(remaining_elements):
                visited_vertices.append(elm)
                graph_queue.append(elm)

    return visited_vertices


if __name__ == "__main__":
    print(breadth_first_traversal(graph, "A"))
