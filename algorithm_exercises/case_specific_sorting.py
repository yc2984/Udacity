def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if ord(left[left_index]) > ord(right[right_index]):
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    # return the ordered, merged list
    return ''.join(merged)


def mergesort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left = string[:mid]
    right = string[mid:]
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def case_sort(string): # [YC] yay!!
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    sorted_string = mergesort(string)
    output = []
    upper_case_index = 0
    lower_case_index = 0
    for index, char in enumerate(string):
        if ord(char) >= 97:  # It means it's lower case
            while ord(sorted_string[lower_case_index]) < 97:
                lower_case_index += 1
            output.append(sorted_string[lower_case_index])
            lower_case_index += 1
        else:
            output.append(sorted_string[upper_case_index])
            upper_case_index += 1
    return ''.join(output)


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")

test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)