"""
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""


def heapify(arr, n, i):  # Down heapify to a max heap

    min_index = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    # compare with left child
    if left_index < n and arr[i] < arr[left_index]:
        min_index = left_index

    # compare with right child
    if right_index < n and arr[min_index] < arr[right_index]:
        min_index = right_index

    # if either of left / right child is the largest node
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]

        heapify(arr, n, min_index)


def heap_sort(arr):
    for i in range(len(arr), -1, -1):
        heapify(arr, len(arr), i)

    # One by one extract elements
    first_arr = []
    second_arr = []

    for i in range(len(arr) - 1, -1, -1):

        max_value = arr[0]
        if i % 2 == 0:
            first_arr.append(str(max_value))
        else:
            second_arr.append(str(max_value))
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return [int(''.join(first_arr)), int(''.join(second_arr))]


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    return heap_sort(input_list)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test cases
# 1
test_function([[1, 2, 3, 4, 5], [531, 42]])
# 2
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# 3
test_function([[0, 0], [0, 0]])
# 4
test_function([[0, 0, 0, 0, 0], [0, 0]])
# 5
test_function([[5, 5, 5, 5, 5, 5], [555, 555]])
# 6
test_function([[5, 0, 5, 0, 5], [550, 50]])