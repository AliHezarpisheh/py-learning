"""
A Binary Search Tree (BST) is a node-based binary tree data structure where each node
has a data, and each node's data is greater than all data in its left subtree and less
than all data in its right subtree. BSTs are useful for searching, insertion, and
deletion operations, all of which can be performed efficiently.
"""

from typing import Any


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


class BinarySearchTree:
    """A class representing a binary search tree (BST)."""

    def __init__(self, root_node: TreeNode | None = None) -> None:
        """
        Initialize the binary search tree with an optional root node.

        Parameters
        ----------
        root_node : TreeNode or None, optional
            The root node of the binary search tree. Default is None.
        """
        self.root_node = root_node

    def get_min(self) -> Any:
        """
        Return the minimum value stored in the binary search tree.

        Returns
        -------
        Any
            The minimum value in the binary search tree.
        """
        current = self.root_node
        while current.left_child:
            current = current.left_child

        return current.data

    def get_max(self) -> Any:
        """
        Return the maximum value stored in the binary search tree.

        Returns
        -------
        Any
            The maximum value in the binary search tree.
        """
        current = self.root_node
        while current.right_child:
            current = current.right_child

        return current.data

    def search(self, data: Any) -> Any:
        """
        Search for a node with the given data in the binary search tree.

        Parameters
        ----------
        data : Any
            The data to search for in the binary search tree.

        Returns
        -------
        Any
            The data if found, otherwise None.
        """
        return self._search_recursive(self.root_node, data)

    def _search_recursive(self, node: TreeNode, data: Any) -> Any:
        """
        Helper method to search for a node with the given data in the binary search tree.

        Parameters
        ----------
        node : TreeNode
            The current node in the binary search tree.
        data : Any
            The data to search for in the binary search tree.

        Returns
        -------
        Any
            The data if found, otherwise None.
        """
        if (node is None) or node.data == data:
            return None if node is None else node.data
        elif node.data > data:
            return self._search_recursive(node.left_child, data)
        else:
            return self._search_recursive(node.right_child, data)

    def delete(self, data: Any) -> None:
        """
        Delete the node with the given data from the binary search tree.

        Parameters
        ----------
        data : Any
            The data of the node to delete from the binary search tree.
        """
        self.root_node = self._delete_recursive(self.root_node, data)

    def _delete_recursive(self, node: TreeNode, data: Any) -> TreeNode:
        """
        Helper method to delete the node with the given data from the binary search tree.

        Parameters
        ----------
        node : TreeNode
            The current node in the binary search tree.
        data : Any
            The data of the node to delete from the binary search tree.

        Returns
        -------
        TreeNode
            The new subtree with the specified node deleted.
        """
        if node is None:
            return node

        if data < node.data:
            node.left_child = self._delete_recursive(node.left_child, data)
        elif data > node.data:
            node.right_child = self._delete_recursive(node.right_child, data)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child

            # Node with two children: Get the in-order successor (smallest in the right subtree)
            node.data = self.get_min(node.right_child).data
            # Delete the in-order successor
            node.right_child = self._delete_recursive(node.right_child, node.data)

        return node


if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)
    #     10
    #    /  \
    #   5    15
    #  / \   / \
    # 3   7 12  18

    bst.delete(10)
