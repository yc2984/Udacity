def staircase(n):
    """
    :param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    TODO - write a recursive function to solve this problem
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    number_of_results = 1
    for first_step_size in range(1, 4):  # first_step_size could be 1, 2, or 3
        number_of_results += staircase(n - first_step_size)
    return number_of_results



def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)


n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)


n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)