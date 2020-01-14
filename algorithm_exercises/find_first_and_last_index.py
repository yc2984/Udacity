def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(target, source):  # This is the solution provided
    index = recursive_binary_search(target, source)
    if not index:
        return -1
    while source[index] == target:
        if index == 0:
            return index
        if source[index-1] == target:
            index -= 1
        else:
            return index


def find_last(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return -1
    while source[index] == target:
        if index == len(source) - 1:
            return index
        if source[index+1] == target:
            index += 1
        else:
            return index


def first_and_last_index(arr, number): # [Yay]
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # Note that you may want to write helper functions to find the start
    # index and the end index
    if len(arr) == 1:
        if arr[0] == number:
            return [0, 0]
        else:
            return [-1, -1]

    return [find_first(number, arr), find_last(number, arr)]


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)


input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)


input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)


input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)