def sqrt(number):
    """
    Calculate the floored square root of a number. The expected time complexity is O(log(n))

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    low = 0
    high = number
    floor_median = (low + high)//2

    while low <= floor_median <= high:
        ceiling_median = floor_median + 1
        floor_result = floor_median * floor_median
        ceiling_result = ceiling_median * ceiling_median

        if floor_result <= number < ceiling_result:
            return floor_median
        elif number >= ceiling_result:
            floor_median += 1
        else:
            floor_median -= 1


# Test cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")