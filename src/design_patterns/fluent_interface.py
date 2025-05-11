"""
A Fluent Interface is an object-oriented API design pattern.
It aims to make code more readable and expressive by chaining method calls in a way that
resembles natural language.

Core Idea
---------
Each method in a fluent interface returns the same object (usually self), allowing
multiple method calls to be "chained" together in a single statement.

Benefits
--------
- Improves readability, especially for configuration or query-building.
- Encourages a declarative style of programming.
- Enables concise and elegant code.

Drawbacks
---------
- Can obscure logic if overused or poorly documented.
- Harder to debug, since multiple actions happen in one line.
"""

from typing import Self


class QueryBuilder:
    def __init__(self) -> None:
        self._query = ""

    def select(self, fields: str) -> Self:
        self._query = f"Select {fields} "
        return self

    def select_from(self, table: str) -> Self:
        self._query += f"FROM {table} "
        return self

    def where(self, condition: str) -> Self:
        self._query += f"WHERE {condition}"  #! SQL INJECTION!
        return self

    def build(self) -> str:
        return self._query.strip()


if __name__ == "__main__":
    query = (
        QueryBuilder()
        .select("id, username, hashed_password")
        .select_from("users")
        .where("username  = 'ali'")
        .build()
    )
    print(query)
