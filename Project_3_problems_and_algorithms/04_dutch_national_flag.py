"""Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_zero_index = 0
    next_two_index = len(input_list) - 1
    index = 0
    while index <= next_two_index:
        if input_list[index] == 0:
            input_list[index] = input_list[next_zero_index]
            input_list[next_zero_index] = 0
            next_zero_index += 1
            index += 1

        elif input_list[index] == 2:
            input_list[index] = input_list[next_two_index]
            input_list[next_two_index] = 2
            next_two_index -= 1

        else:
            index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([0] * 10)
test_function([1] * 10)
test_function([2] * 10)

test_function([1] * 10 + [0] * 10)
