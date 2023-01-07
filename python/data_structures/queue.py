from __future__ import annotations
from typing import Union


class Queue():
    def __init__(self, type=int, max_size=10) -> None:

        self.datatype = type
        self.__max_size = max_size
        self.__queue = []

    def enqueue(self, item):
        if self.isFull():
            raise ValueError("Queue is Full")
        if not isinstance(item, self.datatype):
            raise TypeError("Item should be of type {}".format(self.datatype))
        self.__queue.append(item)

    def dequeue(self) -> Union[Queue.datatype, None]:
        if not self.isEmpty():
            return self.__queue.pop(0)
        return None

    def peek(self) -> Union[Queue.datatype, None]:
        if not self.isEmpty():
            return self.__queue[0]
        return None

    def isEmpty(self) -> bool:
        return len(self.__queue) == 0

    def isFull(self) -> bool:
        return len(self.__queue) == self.__max_size
