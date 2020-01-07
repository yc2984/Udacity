def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(target, source):  # [Yay] But this is over complicated, because the binary search array is searched.
    index = recursive_binary_search(target, source)
    # If the target doesn't exist at all, then return -1
    if index is None:
        return index
    if index == 0:
        return index
    # Check if there's an earlier occurrence
    new_index = recursive_binary_search(target, source[:index], 0)
    # If there isn't any earlier occurrence, return the original index, because it is the first occurrence
    if new_index is None:
        return index
    # If there is an ealier occurrence, the find the earlier index
    return find_first(target, source[:new_index + 1])


def find_first(target, source):  # This is the solution provided
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index

multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple))  # Should return 3
print(find_first(9, multiple))  # Should return None