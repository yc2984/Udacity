# For this exercise we will be using an Adjacency List representation to store the graph.

# Class Node representation.
class Node:
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph():
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


def dfs_recursion_start(self, start_node):
    visited = {}
    self.dfs_recursion(start_node, visited)


def dfs_recursion(self, node, visited):
    if (node == None):
        return False

    visited[node.value] = True
    print(node.value)

    for each in node.children:
        if (each.value not in visited):
            self.dfs_recursion(each, visited)


# Creating a graph as above.
nodeG = Node('G')
nodeR = Node('R')
nodeA = Node('A')
nodeP = Node('P')
nodeH = Node('H')
nodeS = Node('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )

graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)


Graph.dfs_recursion_start = dfs_recursion_start

Graph.dfs_recursion = dfs_recursion

print("search result:", graph1.dfs_recursion_start(nodeG))


