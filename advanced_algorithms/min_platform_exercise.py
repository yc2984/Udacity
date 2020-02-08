# referred to this solution: https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    n = len(arrival)
    arrival.sort()
    departure.sort()
    result = 1
    num_plat = 1
    i = 1  # Number of arrival
    j = 0
    while (i < n and j < n):
        if arrival[i] < departure[j]:
            num_plat += 1
            i += 1
            if (num_plat > result):
                result = num_plat
        else:
            num_plat -= 1
            j += 1
    return result


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)


arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)