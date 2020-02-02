
"""You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target current_value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:"""


def rotated_search(input_list, low, high, target):

    if low >= high:
        if not input_list[low] == target:
            return -1
        else:
            return low

    current_index = (low + high) // 2

    current_value = input_list[current_index]
    if current_value == target:
        return current_index

    elif current_value > input_list[high]:  # the right is the unsorted, the left is sorted

        if input_list[low] <= target < current_value:  # the target is in the left port of the list.
            return rotated_search(input_list, low, current_index - 1, target)
        else:
            return rotated_search(input_list, current_index + 1, high, target)
    elif current_value < input_list[low]:  # The left part is unsorted, the right part is sorted

        if current_value < target <= input_list[high]:  # The target is in the right part of the list
            return rotated_search(input_list, current_index + 1, high, target)
        else:
            return rotated_search(input_list, low, current_index - 1, target)

    else:  # Both sides are sorted

        if current_value > target:  # Go to left
            return rotated_search(input_list, low, current_index - 1, target)
        else:
            return rotated_search(input_list, current_index + 1, high, target)


def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), target(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    return rotated_search(input_list, 0, len(input_list) - 1, target)


def linear_search(input_list, target):
    for index, element in enumerate(input_list):
        if element == target:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]
    if linear_search(input_list, target) == rotated_array_search(input_list, target):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge cases:
# Empty list
test_function([[], -1])
# Non-existing element
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
