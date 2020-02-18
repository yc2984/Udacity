"""### Problem Statements

In an ocean, there are `n` islands some of which are connected via bridges. Travelling over a bridge has some cost attaced with it. Find bridges in such a way that all islands are connected with minimum cost of travelling.

You can assume that there is at least one possible way in which all islands are connected with each other.

You will be provided with two input parameters:

1. `num_islands` = number of islands

2. `bridge_config` = list of lists.
    Each inner list will have 3 elements:
        a. island A
        b. island B
        c. cost of bridge connecting both islands

    Each island is represented using a number

**Example:**
* `num_islands = 4`
* `bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]`

Input parameters explanation:
    1. Number of islands = 4
    2. Island 1 and 2 are connected via a bridge with cost = 1
       Island 2 and 3 are connected via a bridge with cost = 4
       Island 1 and 4 are connected via a bridge with cost = 3
       Island 4 and 3 are connected via a bridge with cost = 2
       Island 1 and 3 are connected via a bridge with cost = 10

In this example if we are connecting bridges like this...
* between 1 and 2 with cost = 1
* between 1 and 4 with cost = 3
* between 4 and 3 with cost = 2

...then we connect all 4 islands with `cost = 6` which is the minimum traveling cost.


### Hint

In addition to using a graph, you may want to use a custom priority queue for solving this problem.

If you do not want to create a custom priority queue, you can use Python's `heapq` implementation.

Using the `heapq` module, you can convert an existing list of items into a heap. The following two functionalities can be very handy for this problem:

1. `heappush(heap, item)` — add `item` to the `heap`
2. `heappop(heap)` — remove the smallest item from the `heap`

Let's look at the above methods in action. We start by creating a list of integers.
"""

import heapq


def create_graph(num_islands, bridge_config):  # [YC] This is what I didn't think of. You need to first create a graph. Recall how to represent a graph.

    graph = [[] for _ in range(num_islands + 1)]
    for bridge in bridge_config:
        island_1, island_2, cost_1_2 = bridge[0], bridge[1], bridge[2]
        graph[island_1].append((island_2, cost_1_2))  # [YC] This is how we are going to represent graph here, with index as the start node, first element in tuple as the destination and the second of the tuple as the cose
        graph[island_2].append((island_1, cost_1_2))
    return graph

# TODO: [YC] why can you ensure all the vertex are connected???
def minimum_cost(graph):  # [YC] This is the key of this problem. I didn't figure out how to solve this, this is integrated with the provided solution.
    start_vertex = 1
    visited = [False for _ in range(len(graph) + 1)]
    heap = [(0, start_vertex)]
    total_cost = 0
    while len(heap) > 0:
        # Always get the vertex with the least cost
        cost, current_vertex = heapq.heappop(heap)
        if visited[current_vertex]:
            continue
        # If the vertex has never been visited before, then visit it:
        #   1) add the cost to total cost
        #   2) add all the neighbor to the heap.
        #   3) mark visited True
        total_cost += cost
        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(heap, (edge_cost, neighbor))
        visited[current_vertex] = True
    return total_cost


# def get_minimum_cost_of_connecting(num_islands, bridge_config):  # [YC] My own trying
#     """
#     :param: num_islands - number of islands
#     :param: bridge_config - bridge configuration as explained in the problem statement
#     return: cost (int) minimum cost of connecting all islands
#     TODO complete this method to returh minimum cost of connecting all islands
#     """
#     # Graph is a list of lists
#     graph = create_graph(num_islands, bridge_config)
#
#     cost_heap = []
#     # Create a heap order by cost
#     for bridge in bridge_config:
#         island_1, island_2, cost_1_2 = bridge[0], bridge[1], bridge[2]
#         heapq.heappush(cost_heap, (cost_1_2, island_1, island_2))
#     # How to judge if all the island are connected?
#     connected = {}
#     total_cost = 0
#     while len(connected) < num_islands and cost_heap:
#         cost, head, tail = cost_heap.pop()
#         if head in connected and tail in connected:
#             pass
#         total_cost += cost
#         connected.update({head: True})
#         connected.update({tail: True})
#     return cost

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)


num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)


num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)