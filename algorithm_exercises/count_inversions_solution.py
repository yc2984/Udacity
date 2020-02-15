def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


def inversion_count_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2

    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_index, mid_index)

    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)

    output = left_answer + right_answer

    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)  # left > right hence it's an inversion # [YC], because left array is sorted, it means all the element in the left array from index left_index to end_one all make an inversion.
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:  # [YC] This means the left array has been exhausted, then we will add everything from the right array.
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:  # [YC] This mean the right array has been exhausted add everything from left array.
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break
    # [YC] this is just to copy the elements from output_list to arr.
    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)


arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)