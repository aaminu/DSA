from __future__ import annotations
from typing import Union


class Queue():
    def __init__(self, type_=int, max_size=10) -> None:

        self.datatype = type_
        self.__max_size = max_size
        self.__queue = []
        self.name = "Queue"

    def enqueue(self, item):
        if self.isFull():
            raise ValueError(f"{self.name} is Full")
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
        return self.size() == 0

    def isFull(self) -> bool:
        return self.size() == self.__max_size

    def size(self) -> int:
        return len(self.__queue)


class Deque(Queue):
    def __init__(self, type_=int, max_size=10) -> None:
        super().__init__(type_, max_size)
        self.name = "Deque"

    def add_front(self, item):
        if self.isFull():
            raise ValueError(f"{self.name} is Full")
        if not isinstance(item, self.datatype):
            raise TypeError(
                "Item should be of type {}".format(self.datatype))

        self._Queue__queue.insert(0, item)

    def add_back(self, item):
        return self.enqueue(item)

    def pop_front(self):
        return self.dequeue()

    def pop_back(self):
        if not self.isEmpty():
            return self._Queue__queue.pop()
        return None
