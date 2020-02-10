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
    mid = (low + high)//2
    while low <= high:
        mid = (low + high)//2
        floor_result = mid * mid

        if floor_result == number:
            return mid
        elif floor_result < number:
            low = mid + 1
        else:
            high = mid-1

    return mid


# Test cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (100 == sqrt(10000)) else "Fail")
print ("Pass" if  (100 == sqrt(10030)) else "Fail")