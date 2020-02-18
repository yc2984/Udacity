from collections import deque


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

# https://knowledge.udacity.com/questions/71717#
def bfs_search(root_node, search_value):  # [YC] I didn't figure it out.
    visited = []
    queue = [root_node]
    visited.append(root_node)

    while len(queue) > 0:
        current_node = queue.pop(0)
        # visited.append(current_node)

        if current_node.value == search_value:
            return current_node
        for child in current_node.children:
            if child not in visited:
                queue.append(child)
                visited.append(child)  # [YC] Note we need to mark the node as visited as soon as we enqueue it, because it might cause problems when a node is child of two adjacent node, see: https://stackoverflow.com/questions/45623722/marking-node-as-visited-on-bfs-when-dequeuing


assert nodeA == bfs_search(nodeS, 'A')
assert nodeS == bfs_search(nodeP, 'S')
assert nodeR == bfs_search(nodeH, 'R')