# [YC] yay! but the time complexity is O(n*k or n^2), not O(n)
def find_index(index, input_list, target):
    sec_indexes = range(index + 1, len(input_list))
    for sec_index in sec_indexes:
        if input_list[index] + input_list[sec_index] == target:
            return [index, sec_index]
    return find_index(index + 1, input_list, target)

def pair_sum_to_zero(input_list, target):
    # TODO: Write pair sum to zero function
    index = 0
    return find_index(index, input_list, target)

def test_function(test_case):
    output = pair_sum_to_zero(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)

test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
test_function(test_case_3)