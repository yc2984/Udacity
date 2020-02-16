class GraphEdge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_u, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_u, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_d, 4)
graph.add_edge(node_c, node_u, 6)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_a, 7)
graph.add_edge(node_i, node_c, 4)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_c, 5)
graph.add_edge(node_t, node_y, 5)
graph.add_edge(node_y, node_i, 4)
graph.add_edge(node_y, node_t, 5)


import math
import heapq


def get_min_distance(start_node, distance_dict, edge):

    old_distance = distance_dict.get(edge.node.value)
    distance = distance_dict.get(start_node.value) + edge.distance
    if not old_distance:
        return None, distance
    else:
        return old_distance, min(old_distance, distance)


def traverse_all_edges_and_update_distance_dict(start_node, distance_dict, distance_heap):

    for edge in start_node.edges:
        old_distance, new_distance = get_min_distance(start_node, distance_dict, edge)
        distance_dict.update({edge.node.value: new_distance})
        if edge.node.value in distance_dict:
            distance_heap.remove((old_distance, edge.node))  # TODO: [YC] question, how can I use heap here? 
        heapq.heappush(distance_heap, (edge.distance, edge.node))


def dijkstra(start_node, end_node):
    if start_node.value == end_node.value:
        return 0
    distance_dict = {start_node.value: 0}
    distance_heap = [(0, start_node)]
    visited = {start_node.value: True}
    # First check all the adjacent nodes of the start_node
    traverse_all_edges_and_update_distance_dict(start_node, distance_dict, distance_heap)

    # Then go to the node with closest distance, add it to visited.
    while distance_heap:
        closest_node = heapq.heappop(distance_heap)[1]
        visited[closest_node.value] = closest_node
        traverse_all_edges_and_update_distance_dict(closest_node, distance_dict, distance_heap)
    return distance_dict.get(end_node.value)


print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(node_u, node_y)))