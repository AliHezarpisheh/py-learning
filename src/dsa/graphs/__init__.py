"""
A graph is a data structure used to represent a set of objects (nodes or
vertices) and the relationships (edges) between them. Graphs are widely used
in various applications like social networks, transportation networks, and
network topology.

**Key Concepts:**

1. **Vertices (Nodes)**: These are the fundamental units or entities in a
   graph. Each vertex can store data and can have zero or more edges
   connecting it to other vertices.

2. **Edges**: These are the connections between vertices. Edges can be directed
   (one-way) or undirected (two-way). They can also have weights, representing
   the cost or distance between vertices.

3. **Adjacency**: Two vertices are adjacent if they are connected by an edge.
   The adjacency list and adjacency matrix are common ways to represent a
   graph:
   - **Adjacency List**: Each vertex stores a list of adjacent vertices. This
     is efficient for sparse graphs.
   - **Adjacency Matrix**: A 2D array where each cell (i, j) indicates the
     presence (and weight) of an edge between vertices i and j. This is
     efficient for dense graphs.

4. **Types of Graphs**:
   - **Undirected Graph**: Edges have no direction. The edge (u, v) is the same
     as (v, u).
   - **Directed Graph (Digraph)**: Edges have a direction. The edge (u, v) is
     not the same as (v, u).
   - **Weighted Graph**: Edges have associated weights.
   - **Unweighted Graph**: Edges have no weights.
   - **Cyclic Graph**: Contains at least one cycle, a path where the first and
     last vertices are the same.
   - **Acyclic Graph**: Contains no cycles. A directed acyclic graph (DAG) is
     commonly used in scheduling.

5. **Traversal**:
   - **Depth-First Search (DFS)**: Explores as far as possible along each
     branch before backtracking.
   - **Breadth-First Search (BFS)**: Explores all neighbors at the present
     depth before moving on to vertices at the next depth level.

6. **Applications**:
   - **Shortest Path**: Algorithms like Dijkstra's and Bellman-Ford find the
     shortest path between vertices.
   - **Connectivity**: Determines if there is a path between vertices.
   - **Network Flow**: Algorithms like Ford-Fulkerson find the maximum flow in
     a flow network.
   - **Topological Sorting**: Orders vertices in a DAG so that for every edge
     (u, v), vertex u comes before v.

**Advantages**:
- Flexible representation of relationships between objects.
- Efficient algorithms for traversal, pathfinding, and network flow.

**Disadvantages**:
- Can be complex to implement and manage, especially with large datasets.
- Memory consumption can be high for dense graphs when using adjacency matrix.

Graphs are foundational in computer science for modeling and solving problems
in various domains.
"""
