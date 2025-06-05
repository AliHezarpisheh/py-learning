# --------- singledispatch ---------
from functools import singledispatchmethod


class Printer:
    @singledispatchmethod
    def show(self, value: int | str) -> None:
        print("Unsupported Type")

    @show.register
    def _(self, value: int) -> None:
        print(f"Integer: {value}")

    @show.register
    def _(self, value: str) -> None:
        print(f"String: {value}")


# --------- overload ---------
from typing import overload


class Calculator:
    @overload
    def add(self, a: int, b: int) -> int:
        ...

    @overload
    def add(self, a: str, b: str) -> str:
        ...

    @overload
    def add(self, a: int, b: int, *args: int) -> int:
        ...

    @overload
    def add(self, **kwargs: int) -> int:
        ...

    def add(
        self,
        a: int | str | None = None,
        b: int | str | None = None,
        *args: int,
        **kwargs: int,
    ) -> int | str:
        if isinstance(a, int) and isinstance(b, int) and not args and not kwargs:
            return a + b
        elif isinstance(a, str) and isinstance(b, str) and not args and not kwargs:
            return str(int(a) + int(b))
        elif isinstance(a, int) and isinstance(b, int) and args and not kwargs:
            return a + b + sum(args)
        elif not (a or b) and kwargs:
            return sum(kwargs.values())
        else:
            raise NotImplementedError("Unsupported input type")
