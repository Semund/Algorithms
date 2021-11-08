from pprint import pprint

graph = {
    'start': {'A': 5, 'B': 2},
    'A': {'C': 4, 'D': 2},
    'B': {'A': 8, 'D': 7},
    'C': {'D': 6, 'end': 3},
    'D': {'end': 1},
    'end': {}
}

inf = float('inf')

costs = {
    'A': 5,
    'B': 2,
    'C': inf,
    'D': inf,
    'end': inf
}

parents = {
    'start': None,
    'A': 'start',
    'B': 'start',
    'C': None,
    'D': None,
    'end': None
}

visited = []


def find_lowest_node(costs):
    lowest_node_cost = inf
    lowest_node = None
    for node in costs.keys():
        if costs[node] < lowest_node_cost and node not in visited:
            lowest_node_cost = costs[node]
            lowest_node = node
    return lowest_node


node = find_lowest_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    visited.append(node)
    node = find_lowest_node(costs)



if parents['end'] is not None:
    node = 'end'
    while parents[node] is not None:
        print(node, end=" <---- ")
        node = parents[node]
    print(node)
    print(costs['end'])