"""Module for a simple hash table implementation in Python."""

from typing import Any


class HashItem:
    """Class representing a key-value pair for the hash table."""

    def __init__(self, key: str, value: Any) -> None:
        """
        Initialize a HashItem with a key and a value.

        Parameters
        ----------
        key : str
            The key for the hash item.
        value : Any
            The value associated with the key.
        """
        self.key = key
        self.value = value


class HashTable:
    """Class representing a simple hash table."""

    def __init__(self) -> None:
        """Initialize the hash table with a fixed size and empty slots."""
        self.size = 256
        self.slots = [None for _ in range(self.size)]
        self.count = 0

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value for a given key in the hash table.

        Parameters
        ----------
        key : str
            The key for which to set the value.
        value : Any
            The value to be set for the given key.
        """
        self.put(key, value)

    def __getitem__(self, key: str) -> Any:
        """
        Get the value associated with a given key in the hash table.

        Parameters
        ----------
        key : str
            The key for which to get the value.

        Returns
        -------
        Any
            The value associated with the given key.
        """
        return self.get(key)

    def _hash(self, key: str) -> int:
        """
        Compute the hash value for a given key.

        Parameters
        ----------
        key : str
            The key to hash.

        Returns
        -------
        int
            The hash value of the key.
        """
        mul = 1
        hv = 0
        for ch in key:
            hv += mul * ord(ch)
            mul += 1
        return hv % self.size

    def put(self, key: str, value: Any) -> None:
        """
        Insert a key-value pair into the hash table.

        Parameters
        ----------
        key : str
            The key to be inserted.
        value : Any
            The value to be associated with the key.
        """
        hash_item = HashItem(key, value)
        hashed_key = self._hash(key)

        # Handling collision.
        while self.slots[hashed_key] is not None:
            if self.slots[hashed_key].key == key:
                break
            hashed_key = (hashed_key + 1) % self.size
        if self.slots[hashed_key] is None:
            self.count += 1

        self.slots[hashed_key] = hash_item

    def get(self, key: str) -> Any:
        """
        Retrieve the value associated with a given key from the hash table.

        Parameters
        ----------
        key : str
            The key for which to retrieve the value.

        Returns
        -------
        Any
            The value associated with the key, or None if the key is not found.
        """
        hashed_key = self._hash(key)
        while self.slots[hashed_key].key is not None:
            if self.slots[hashed_key].key == key:
                return self.slots[hashed_key].value
            hashed_key = (hashed_key + 1) % self.size
        return None
