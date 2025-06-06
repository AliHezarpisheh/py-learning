from functools import total_ordering


@total_ordering
class Person:
    def __init__(self, age: int) -> None:
        self.age = age

    def __eq__(self, value: "Person") -> bool:
        return self.age == value.age

    def __lt__(self, value: "Person") -> bool:
        return self.age < value.age


if __name__ == "__main__":
    jack = Person(age=20)
    sam = Person(age=21)
