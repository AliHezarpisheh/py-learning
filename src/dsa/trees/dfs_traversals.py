from typing import Generator, Any


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


def inorder_traversal(root_node: TreeNode) -> None:
    """
    Perform an inorder traversal on the binary tree rooted at 'root_node'.

    Parameters
    ----------
    root_node : TreeNode
        The root node of the binary tree to traverse.
    """
    current = root_node
    if current is None:
        return None
    inorder_traversal(current.left_child)
    print(current.data)
    inorder_traversal(current.right_child)


def preorder_traversal(root_node: TreeNode) -> None:
    """
    Perform a preorder traversal on the binary tree rooted at 'root_node'.

    Parameters
    ----------
    root_node : TreeNode
        The root node of the binary tree to traverse.
    """
    current = root_node
    if current is None:
        return None
    print(current.data)
    preorder_traversal(current.left_child)
    preorder_traversal(current.right_child)


def postorder_traversal(root_node: TreeNode) -> None:
    """
    Perform a postorder traversal on the binary tree rooted at 'root_node'.

    Parameters
    ----------
    root_node : TreeNode
        The root node of the binary tree to traverse.
    """
    breakpoint()
    current = root_node
    if current is None:
        return None
    postorder_traversal(current.left_child)
    postorder_traversal(current.right_child)
    print(current.data)


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
    B.right_child = E
    C.right_child = F

    print("Inorder Traversal:")
    inorder_traversal(A)  # G-D-H-B-E-A-C-F

    print("\nPreorder Traversal:")
    preorder_traversal(A)  # A-B-D-G-H-E-C-F

    print("\nPostorder Traversal:")
    postorder_traversal(A)  # G-D-H-B-E-A-C-F
