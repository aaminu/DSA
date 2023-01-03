""" Breadth First Search Algorithm (Graph)"""

from collections import deque
from typing import Callable, Union


def breadth_first(graph: dict, id: str, validator: Callable, query_key, valid_value) -> Union[dict, None]:
    queue = deque()
    queue.extend(graph.get(id, []))
    searched = []
    while queue:
        search_item = queue.popleft()
        if search_item["id"] in searched:
            continue
        if validator(search_item, query_key, valid_value):
            return search_item
        else:
            queue.extend(graph[search_item["id"]])
            searched.append(search_item["id"])
    return None
