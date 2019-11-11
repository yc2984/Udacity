def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    print("input arr", arr)

    def _add_one(index, arr):
        arr[index] += 1
        if arr[index] < 10:
            arr[index] += 1
            return arr

        arr[index] = 0
        while index > 0:
            index -= 1
            return _add_one(index, arr)  # NOTE: This is where I took most time to figure out. You need to return _add_one
        # when it's the first element of the array
        arr.insert(0, 1)
        return arr

    return _add_one(len(arr) - 1, arr)


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")



arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)