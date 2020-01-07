def the_recursion(array, target, start_index, end_index):  # [Yay]!
    if start_index > end_index:  # Equal still is okay
        return -1
    mid_index = (start_index + end_index) // 2
    if target == array[mid_index]:
        return mid_index
    elif target < array[mid_index]:
        return the_recursion(array, target, start_index, mid_index - 1)
    else:
        return the_recursion(array, target, mid_index + 1, end_index)


def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    return the_recursion(array, target, 0, len(array) - 1)


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)


# Test case 2
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 12
index = -1
test_case = [array, target, index]
test_function(test_case)

# Test case 3
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
index = 10
test_case = [array, target, index]
test_function(test_case)