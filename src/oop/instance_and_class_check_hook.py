import abc


class BirdMeta(abc.ABCMeta):
    def __instancecheck__(self, instance: object) -> bool:
        return hasattr(instance, "fly") and hasattr(instance, "sing")

    def __subclasscheck__(self, subclass: object) -> bool:
        return hasattr(subclass, "fly") and hasattr(subclass, "sing")


class Bird(metaclass=BirdMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        if hasattr(subclass, "fly") and hasattr(subclass, "sing"):
            return True
        raise NotImplementedError


class Duck:
    def fly(self):
        ...

    def sing(self):
        ...


class Plane:
    def fly(self):
        ...

    def shoot(self):
        ...
