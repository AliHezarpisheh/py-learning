"""
BFS traverses a binary tree level by level. It starts at the root and explores all the
nodes at the present depth level before moving on to nodes at the next depth level.

How it works:

Initialization: Begin at the root node.
Queue: Use a queue to keep track of nodes. Initially, enqueue the root node.
Traversal:
Dequeue a node from the front of the queue.
Visit this node (process it according to your needs).
Enqueue the node's children (first the left child, then the right child) to the queue.
Repeat the above steps until the queue is empty.

Characteristics:

Level-order: BFS is also called level-order traversal because it processes nodes level
by level. Space Complexity: It requires more memory compared to DFS because it stores
all the nodes at a given level. For a complete binary tree, the space complexity can go
up to O(n/2) ≈ O(n) where n is the number of nodes. Application: BFS is useful when the
shortest path is needed (like in unweighted graphs) and for systems that need to process
nodes level by level.
"""

from collections import deque
from typing import Any, Generator


class TreeNode:
    """Represent a Node in a tree structure."""

    def __init__(self, data: Any):
        """Instantiate a node with the given data."""
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return f"TreeNode <{self.data}>"

    def __repr__(self) -> str:
        """Return a string representation of the node for debugging purposes."""
        return f"TreeNode ({self.data})"


def breadth_first_traversal(root_node: TreeNode) -> Generator[Any, None, None]:
    """
    Perform a breadth-first traversal on the binary tree rooted at 'root_node'.

    Parameters
    ----------
    root_node : TreeNode
        The root node of the binary tree to traverse.

    Yields
    ------
    Any
        The data of each node in breadth-first order.
    """
    if root_node is None:
        return None

    queue = deque()
    queue.append(root_node)

    while queue:
        current_node = queue.popleft()
        yield current_node.data
        if current_node.left_child is not None:
            queue.append(current_node.left_child)
        if current_node.right_child is not None:
            queue.append(current_node.right_child)


if __name__ == "__main__":
    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    E = TreeNode("E")
    F = TreeNode("F")
    G = TreeNode("G")
    H = TreeNode("H")

    A.left_child = B
    A.right_child = C
    B.left_child = D
    D.left_child = G
    D.right_child = H
    C.left_child = E
    C.right_child = F

    print("Breadth-First Traversal:")
    for node in breadth_first_traversal(A):
        print(node)
