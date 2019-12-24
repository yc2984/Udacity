class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Returns true if there is a path from
# root to the given node. It also
# populates 'arr' with the given path
def value_in_tree(node, value, arr):
    # Get inspired by: https://www.geeksforgeeks.org/print-path-root-given-node-binary-tree/
    """
    :param node:
    :param value:
    :param arr:
    :return:
    """
    if not node:
        return False, arr
    arr.append(node.data)
    if node.data == value:
        return True, arr
    if value_in_tree(node.left, value, arr)[0] or value_in_tree(node.right, value, arr)[0]:
        return True, arr
    # [YC] this is the part that I didn't figure out.
    # required node does not lie either in
    # the left or right subtree of the current
    # node. Thus, remove current node's value
    # from 'arr'and then return false
    arr.pop()
    return False, arr


def path_from_root_to_node(root, data):
    """
    1. If root = NULL, return false.
    2. push the root’s data into arr[].
    3. if root’s data = x, return true.
    4. if node x is present in root’s left or right subtree, return true.
    5. Else remove root’s data value from arr[] and return false.

    :param: root - root of binary tree
    :param: data - value (representing a node)
    TODO: complete this method and return a list containing values of each node in the path
    from root to the data node
    """
    return value_in_tree(root, data, [])

from queue import Queue


def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree
    """
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root


def test_function(test_case):
    arr = test_case[0]
    data = test_case[1]
    solution = test_case[2]
    root = convert_arr_to_binary_tree(arr)
    output = path_from_root_to_node(root, data)[1]
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
data = 5
solution = [1, 2, 5]

test_case = [arr, data, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 11
solution = [1, 3, 4, 6, 10, 11]

test_case = [arr, data, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 8
solution = [1, 3, 5,8]

test_case = [arr, data, solution]
test_function(test_case)


