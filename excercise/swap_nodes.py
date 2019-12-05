class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: left_index - indicates position
    :param: right_index - indicates position
    return: head of updated linked list with nodes swapped
    TODO: complete this function and swap nodes present at left_index and right_index
    Do not create a new linked list

    1) the next node of node_before_left is the next of the next of itself, pointing 5 --> 6
    2) the



   TODO [YC] reproduce the solution 20191119
    """

    current_node = head
    counter = 0
    while current_node is not None:  #
        counter += 1  # [0, 1, 2,  3,  4,  5,  6]
        if counter == left_index:  # say i = 3, j =5.  [3, 4, 5, '2', 6, '1', 9], head = 3, counter = 0  # (5)
            # current (5)
            left_node = current_node.next  # (2)
            node_before_left = current_node  # (5)
            node_right_next = left_node.next  # (6)

        elif counter == right_index:
            # current (6)
            right_node = current_node.next # ('1')
            left_node.next = right_node.next  # left node is '2', and the next of '2' is 9
            node_before_left.next = right_node  # node before left node is 5, 5 and then '1'
            right_node.next = node_right_next
            current_node.next = left_node
        print("current node", current_node.value)
        current_node = current_node.next
    # TODO: check if left previous is None
    return head


def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)


# arr = [3, 4, 5, 2, 6, 1, 9]
# left_index = 2
# right_index = 4
# head = create_linked_list(arr)
# test_case = [head, left_index, right_index]
# updated_head = test_function(test_case)
#
#
# arr = [3, 4, 5, 2, 6, 1, 9]
# left_index = 0
# right_index = 1
# head = create_linked_list(arr)
# test_case = [head, left_index, right_index]
# updated_head = test_function(test_case)