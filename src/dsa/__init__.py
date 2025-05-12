"""
Data Structures and Algorithms

Data Structures and Algorithms form the computational foundation for problem-solving,
resource management, and performance optimization in software systems.

Data Structures
---------------
A data structure is a formal way of organizing and storing data so that it can be
accessed and modified efficiently. The choice of data structure directly affects the
time and space complexity of an algorithm.

A data structure is a formal way of organizing and storing data so that it can be
accessed and modified efficiently. The choice of data structure directly affects the
time and space complexity of an algorithm.

Categories:
- Linear Data Structures: Memory is arranged sequentially.
    Array: Fixed-size contiguous memory; O(1) access; O(n) insertion/deletion.
    Linked List: Dynamic memory; O(n) access; O(1) insertion/deletion at head.
    Stack: LIFO; O(1) push/pop; used in recursion, parsing, etc.
    Queue / Deque: FIFO / double-ended; useful in scheduling, BFS, etc.

- Non-Linear Data Structures:
    Tree: Hierarchical; used in databases (e.g., B-trees),
    memory allocation (segment trees).
    Binary Trees, Binary Search Trees (BST), AVL Trees, Heaps, Segment Trees, Tries.
    Graph: Node-edge structure; models networks (e.g., social networks, maps).

- Hash-Based Structures:
    Hash Tables / Hash Maps / Hash Sets: O(1) average access; used in indexing, caching.

Algorithms
----------
An algorithm is a finite sequence of steps to solve a well-defined computational
problem. Efficiency is evaluated in terms of time and space
complexity (Big-O, Big-Ω, Big-Θ).

Categories: Divide and Conquer, Dynamic Programming, Greedy Algorithms, Backtracking,
Sorting, Searching, Graph Algorithms, String Algorithms.

Core Goals When Studying DSA
----------------------------
- Space-Time Trade-offs: Know when to use space to gain time and vice versa.
- Algorithm-Data Structure Fit: Pair the right structure with the right algorithm.
- Understand Underlying Mechanisms: Eg. why quicksort is fast in practice despite
  worst-case O(n²).
- Real-World Mapping: Understand how trees power DOMs and indexes, graphs power routing,
  DP powers optimization, etc.
"""