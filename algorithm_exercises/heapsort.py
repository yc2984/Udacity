def helper_function(arr):

    if len(arr) <= 1:
        return arr.pop()
    # First build a max heap
    heapify(arr, len(arr), 0)
    # Then switch the head with the last element of the max heap
    max_value = arr[0]
    arr[0] = arr[-1]
    arr[-1] = max_value
    # Then remove the current last element (previous head, which is the maximum)
    return arr.pop()


def heapsort(arr):
    final_result = []
    while len(arr) >= 1:
        final_result.insert(helper_function(arr), 0)


def heapify(arr, num_element, current_index):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """

    while current_index <= num_element:  # TODO; when to upheafy and when to downpify??
        parent = arr[current_index]
        left_child_index = 2 * current_index + 1
        right_child_index = 2 * current_index + 2
        left = right = None
        if left_child_index < num_element:
            left = arr[left_child_index]
        if right_child_index < num_element:
            right = arr[right_child_index]
        max_value = parent
        if left:
            max_value = left if left > parent else parent
        if right:
            max_value = max_value if max_value > right else right
        if max_value == parent:
            return
        if max_value == left:
            arr[current_index] = left
            arr[left_child_index] = parent
            current_index = left_child_index
            heapify(arr, num_element, current_index)
        if max_value == right:
            arr[current_index] = right
            arr[right_child_index] = left
            current_index = left_child_index
            heapify(arr, num_element, current_index)


def _up_heapify(arr, num_element, current_index):
    # print("inside heapify")
    current_index = len(arr) - 1
    child_index = current_index
    while child_index >= 1:
        parent_index = (child_index - 1) // 2
        parent_element = arr[parent_index]
        child_element = arr[child_index]
        if parent_element < child_element:
            arr[parent_index] = child_element
            arr[child_index] = parent_element
            child_index = parent_index
        else:
            break


def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]

test_case = [arr, solution]

test_function(test_case)


# arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
# solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# test_case = [arr, solution]
# test_function(test_case)
#
# arr = [99]
# solution = [99]
# test_case = [arr, solution]
# test_function(test_case)
#
# arr = [0, 1, 2, 5, 12, 21, 0]
# solution = [0, 0, 1, 2, 5, 12, 21]
# test_case = [arr, solution]
# test_function(test_case)
