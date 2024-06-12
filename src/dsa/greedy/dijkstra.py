"""
Functions for finding the shortest path in a graph using Dijkstra's algorithm.
"""


def get_shortest_distance(
    table: dict[str, list[int | float, str | None]], vertex: str
) -> int:
    """Get the shortest distance in the table for a given vertex."""
    shortest_distance = table[vertex][DISTANCE]
    return shortest_distance


def set_shortest_distance(
    table: dict[str, list[int | float, str | None]],
    vertex: str,
    new_distance: int = int,
) -> None:
    """Set the shortest distance in the table for a given vertex."""
    table[vertex][DISTANCE] = new_distance


def set_previous_node(
    table: dict[str, list[int | float, str | None]], vertex: str, previous_node: str
) -> None:
    """Set the previous node in the table for a given vertex."""
    table[vertex][PREVIOUS_NODE] = previous_node


def get_distance(
    graph: dict[str, dict[str, int]], first_vertex: str, second_vertex: str
) -> int:
    """Get the distance between two vertices in the graph."""
    return graph[first_vertex][second_vertex]


def get_next_node(
    table: dict[str, list[int | float, str | None]], visited_nodes: list[str]
) -> str:
    """Get the next node to visit in the graph."""
    unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes)))
    assumed_min = table[unvisited_nodes[0]][DISTANCE]
    min_vertex = unvisited_nodes[0]
    for node in unvisited_nodes:
        if table[node][DISTANCE] < assumed_min:
            assumed_min = table[node][DISTANCE]
            min_vertex = node
    return min_vertex


def find_shortest_path(
    graph: dict[str, dict[str, int]],
    table: dict[str, list[int | float, str | None]],
    origin: str,
) -> list:
    """Find the shortest path from the origin to all other vertices in the graph."""
    visited_nodes = []
    current_node = origin
    while True:
        adjacent_nodes = graph[current_node]
        if set(adjacent_nodes).issubset(set(visited_nodes)):
            pass
        else:
            unvisited_nodes = set(adjacent_nodes).difference(set(visited_nodes))
            for vertex in unvisited_nodes:
                distance_from_starting_node = get_shortest_distance(table, vertex)
                if distance_from_starting_node == INFINITY and current_node == origin:
                    total_distance = get_distance(graph, vertex, current_node)
                else:
                    total_distance = get_shortest_distance(
                        table, current_node
                    ) + get_distance(graph, vertex, current_node)

                if total_distance < distance_from_starting_node:
                    set_shortest_distance(table, vertex, total_distance)
                    set_previous_node(table, vertex, current_node)
        visited_nodes.append(current_node)
        if len(visited_nodes) == len(table):
            break
        current_node = get_next_node(table, visited_nodes)
    return table


if __name__ == "__main__":
    graph = dict()
    graph["A"] = {"B": 5, "D": 9, "E": 2}
    graph["B"] = {"A": 5, "C": 2}
    graph["C"] = {"B": 2, "D": 3}
    graph["D"] = {"A": 9, "F": 2, "C": 3}
    graph["E"] = {"A": 2, "F": 3}
    graph["F"] = {"E": 3, "D": 2}

    table = dict()
    table = {
        "A": [0, None],
        "B": [float("inf"), None],
        "C": [float("inf"), None],
        "D": [float("inf"), None],
        "E": [float("inf"), None],
        "F": [float("inf"), None],
    }

    DISTANCE = 0
    PREVIOUS_NODE = 1
    INFINITY = float("inf")

    shortest_distance_table = find_shortest_path(graph, table, "A")

    for k in sorted(shortest_distance_table):
        print("{} - {}".format(k, shortest_distance_table[k]))
