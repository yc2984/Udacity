"""Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        print("cannot find max min for empty list")
        return None, None
    if len(ints) == 1:
        return ints[0], ints[0]
    max_value = ints[0]
    min_value = ints[0]
    for number in ints:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
    return min_value, max_value

## Example Test Case of Ten Integers
# Test case 1
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Test case 2
l = [i for i in range(0, 100)]
random.shuffle(l)
print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")


# Test case 3 negative number
l = [i for i in range(0, -100, -1)]
random.shuffle(l)
print ("Pass" if ((-99, 0) == get_min_max(l)) else "Fail")

# Test case 4 empty ligst
l = []
random.shuffle(l)
print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")

# Test case 5, array with only 1 element
l = [5]
random.shuffle(l)
print ("Pass" if ((5, 5) == get_min_max(l)) else "Fail")