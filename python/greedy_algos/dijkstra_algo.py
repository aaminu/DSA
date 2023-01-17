""" Dijkstra Alogrithm (Graph)"""


def get_costs(graph: dict, start_node: any) -> dict:
    cost = {}
    for node in graph:
        cost[node] = graph[start_node].get(node, float("inf"))
    cost.pop(start_node)
    return cost


def get_parents(graph: dict, start_node: any) -> dict:
    parent = {}
    for node in graph:
        parent[node] = None
    for key in graph[start_node]:
        parent[key] = start_node
    parent.pop(start_node)
    return parent


def get_finish_connect_nodes(graph: dict, finish_node: any):
    connected_nodes = []
    for node in graph:
        if finish_node in graph[node].keys():
            connected_nodes.append(node)
    return connected_nodes


def find_lowest_cost_node(costs: dict, processed: list):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if (cost < lowest_cost) and (node not in processed):
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_alogrithm(graph: dict, start_node: any, end_node: any):
    costs = get_costs(graph, start_node)
    parents = get_parents(graph, start_node)
    end_node_parents = get_finish_connect_nodes(graph, end_node)
    processed = []

    node = find_lowest_cost_node(costs, processed)
    while (node is not None) and (end_node_parents):
        cost = costs[node]
        neighbor = graph[node]
        for n in neighbor.keys():
            new_cost = cost + neighbor[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        try:
            end_node_parents.remove(node)
        except ValueError:
            pass
        node = find_lowest_cost_node(costs, processed)
    return {"cost": costs, "parent": parents}
