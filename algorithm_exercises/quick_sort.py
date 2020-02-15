def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index

#
items = [8, 3, 1, 7, 0, 10, 2]
# pivot_index = sort_a_little_bit(items, 0, len(items) - 1)
# print(items)
# print('pivot index %d' % pivot_index)


def quick_sort(arr, start, end):  # [YC] Yay, although I don't quite understand it.
    if start >= end:
        return arr
    pivot_index = sort_a_little_bit(arr, start, end)

    quick_sort(arr, start, pivot_index - 1)

    quick_sort(arr, pivot_index + 1, end)

    return arr


sorted_list = quick_sort(items, 0, len(items) - 1)
print(sorted_list)