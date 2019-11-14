def nth_row_pascal(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    previous_row = [1, 1]    # n = 2, --> [1, 2, 1]
    current_row = [1]
    for i in range(0, n+1, 1):  # To calculate the n th row, we need to calculate all the rows before it, starting from row 1
        current_row = [1]
        for j in range(1, i, 1):  # This is calculating the i th row, which will have i+1 element, and the first and last one is both 1, so we only need to calculate i - 1 element
            current_row.append(previous_row[j - 1] + (previous_row[j] if len(previous_row) > j else 0))

        current_row.append(1)
        previous_row = current_row

    return current_row


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")



# n = 0
# solution = [1]
#
# test_case = [n, solution]
# test_function(test_case)

#
# n = 1
# solution = [1, 1]
#
# test_case = [n, solution]
# test_function(test_case)


n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)


n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)


n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)


n = 5
solution = [1, 5, 10, 10, 5, 1]

test_case = [n, solution]
test_function(test_case)



n = 6
solution = [1, 6, 15, 20, 15, 6, 1]

test_case = [n, solution]
test_function(test_case)