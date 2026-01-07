"""Module containing shitty ahh code, don't pay attention please:)."""

class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds single int
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> list["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.nested_list = nestedList
        self._flatten_items = []

    def next(self) -> int | None:
        if self._flatten_items:
            return self._flatten_items.pop(0)

        item = self.nested_list.pop(0)
        if item.isInteger():
            return item.getInteger()

        items = self._flat_list(items=item.getList())
        self._flatten_items = items
        if not self._flatten_items:
            return self.next()
        return self._flatten_items.pop(0)

    def hasNext(self) -> bool:
        if self._flatten_items:
            return True

        has_next = False
        for item in self.nested_list:
            if item.isInteger():
                has_next = True
                break
            else:
                has_next = self._is_item_list_truthy(item.getList())
                if has_next:
                    break
        print(has_next)
        return has_next

    def _is_item_list_truthy(self, items) -> bool:
        is_truthy = False
        for item in items:
            if item.isInteger():
                is_truthy = True
                break
            else:
                is_truthy = self._is_item_list_truthy(items=item.getList())
                if is_truthy:
                    break
        return is_truthy

    def _flat_list(self, items: list[NestedInteger]) -> list[int]:
        result = []
        for item in items:
            if item.isInteger():
                result.append(item.getInteger())
            else:
                result.extend(self._flat_list(items=item.getList()))
        return result
