"""
Protocol is a feature from Python type system (introduced in PEP 544).

It supports structural subtyping—also called "duck typing"—in a type-safe way. It allows
you to define interfaces that other classes can conform to without inheritance. If a
class has the required methods/attributes, it implicitly conforms to the protocol.

Think of Protocol as 'ABC (Abstract Base Class) without inheritance requirements.'

Key Points
----------
- Protocols can define methods and attributes.
- Protocols can be explicit (inheriting from the protocol) or implicit
  (just having the right structure).
- They're used purely for type checking—they don't affect runtime behavior.
- To allow runtime checking (like isinstance(x, Protocol)), you need @runtime_checkable.
"""

from typing import Protocol, runtime_checkable

@runtime_checkable
class Animal(Protocol):
    def eat(self) -> None: ...


class Cat:
    def eat(self) -> None:
        print("Cat is eating...")


class Dog: ...


def eat(animal: Animal) -> None:
    animal.eat()


if __name__ == "__main__":
    cat = Cat()
    dog = Dog()
    eat(cat)
    eat(dog)
