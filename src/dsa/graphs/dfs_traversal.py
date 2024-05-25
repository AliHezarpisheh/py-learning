"""
Depth-First Search (DFS) is a graph traversal algorithm that explores as 
far as possible along each branch before backtracking. Starting from a 
source node, it explores each branch to its deepest point before moving to 
the next branch. This approach can be implemented using a stack data 
structure, either explicitly with an iterative method or implicitly with 
recursion. DFS is useful for solving problems like finding connected 
components, topological sorting, and detecting cycles in a graph. Its 
time complexity is O(V + E), where V is the number of vertices and E is the 
number of edges.
"""

graph = dict()
graph["A"] = ["B", "S"]
graph["B"] = ["A"]
graph["S"] = ["A", "G", "C"]
graph["D"] = ["C"]
graph["G"] = ["S", "F", "H"]
graph["H"] = ["G", "E"]
graph["E"] = ["C", "H"]
graph["F"] = ["C", "G"]
graph["C"] = ["D", "S", "E", "F"]


def depth_first_traversal(graph: dict[str, list[str]], root: str) -> list[str]:
    """
    Perform depth-first traversal on a graph.

    Parameters
    ----------
    graph : dict[str, list[str]]
        The graph represented as an adjacency list.
    root : str
        The starting vertex for the traversal.

    Returns
    -------
    list[str]
        The list of vertices visited in depth-first order.
    """
    visited_vertices = []
    graph_stack = []  # Think of it as a stack:)

    graph_stack.append(root)
    node = root
    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
            first_adj_node = sorted(remaining_elements)[0]
            node = first_adj_node
            graph_stack.append(node)

    return visited_vertices


print(depth_first_traversal(graph, "A"))
