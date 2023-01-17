from __future__ import annotations
from typing import Union


class Stack():
    def __init__(self, type=int, max_size=10) -> None:

        self.datatype = type
        self.__max_size = max_size
        self.__stack = []

    def push(self, item):
        if self.isFull():
            raise ValueError("Stack is Full")
        if not isinstance(item, self.datatype):
            raise TypeError("Item should be of type {}".format(self.datatype))
        self.__stack.append(item)

    def pop(self) -> Union[Stack.datatype, None]:
        if not self.isEmpty():
            return self.__stack.pop()
        return None

    def peek(self) -> Union[Stack.datatype, None]:
        if not self.isEmpty():
            return self.__stack[-1]
        return None

    def isEmpty(self) -> bool:
        return len(self.__stack) == 0

    def isFull(self) -> bool:
        return len(self.__stack) == self.__max_size
