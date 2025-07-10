"""  
The pickle module serializes Python objects into byte streams (pickling) and  
deserializes them back (unpickling). WARNING: Unpickling untrusted data is  
unsafe. Use for trusted sources only.  

Customize serialization with __getstate__ (controls what gets pickled) and  
__setstate__ (handles unpickling). Example below excludes passwords for  
security.  
"""


class User:
    """User object with controlled pickle serialization (excludes password)."""

    def __init__(self, username: str, password: str) -> None:
        """Initialize user with username and password."""
        self.username = username
        self._password = password

    def __getstate__(self) -> dict[str, str]:
        """Return state without password for secure pickling."""
        state = self.__dict__.copy()
        del state["_password"]
        return state

    def __setstate__(self, state: dict[str, str]) -> None:
        """Restore state and set password to None when unpickled."""
        self.__dict__.update(state)
        self._password = None


if __name__ == "__main__":
    import pickle

    user = User(username="test", password="test")
    pickled_user = pickle.dumps(user)
    original_user = pickle.loads(pickled_user)

    assert original_user.username == "test"
    assert original_user._password is None

    with open("pickled_user", mode="wb") as pickling_file:
        pickle.dump(user, pickling_file)

    with open("pickled_user", mode="rb") as pickling_file:
        original_user = pickle.load(pickling_file)

    assert original_user.username == "test"
    assert original_user._password is None
