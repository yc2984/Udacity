"""Write a function that takes an input array (or Python list) consisting of only 0s, 1s, and 2s, and sorts that array in a single traversal.

Note that if you can get the function to put the 0s and 2s in the correct positions, this will aotumatically cause the 1s to be in the correct positions as well."""


def sort_012(input_list):  # [YC] I solved 60%
    next_pos_zero = 0
    next_pos_two = len(input_list) - 1
    index = 0
    while index <= next_pos_two:
        if input_list[index] == 0:
            input_list[index] = input_list[next_pos_zero]
            input_list[next_pos_zero] = 0
            next_pos_zero += 1
            index += 1  # [YC] index += 1, because we are only moving the zero in front of the input_list[next_pos_zero], which is for sure 1, because if it's a 2, if would be already moved to the end, so we are done evaluating it.

        elif input_list[index] == 2:  # [YC] This one front_index += 1 is not required, because we exchanged the front_index with the element at next_pos_2 which still has to be evaluated.
            input_list[index] = input_list[next_pos_two]
            input_list[next_pos_two] = 2
            next_pos_two -= 1
        else:
            index += 1


def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)