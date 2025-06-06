import operator


# ---- attrgetter ----
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"User(name={self.name}, age={self.age})"


operator.attrgetter("age")(User(name="Jack", age=24))
users = [User("Ali", 21), User("Zara", 19)]
sorted_users = sorted(users, key=operator.attrgetter("age"))


# ---- itemgetter ----
operator.itemgetter("age")({"name": "Ali", "age": 20})
items = [{"name": "Ali", "age": 21}, {"name": "Zara", "age": 19}]
sorted_items = sorted(items, key=operator.itemgetter("age"))


# ---- methodcaller ----
operator.methodcaller("lower")("HI")
names = ["Ali", "Jack"]
lowered_names = list(map(operator.methodcaller("lower"), names))
