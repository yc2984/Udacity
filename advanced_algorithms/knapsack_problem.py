"""Now that you saw the dynamic programming solution for the knapsack problem, it's time to implement it.
Implement the function max_value to return the maximum value given the items (items) and the maximum weight of the knapsack (knapsack_max_weight).
The items variable is the type Item, which is a named tuple."""


import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight=None, items=None):
    """
    Get the maximum value of the knapsack.
    """
    # items_in_bag = collections.defaultdict(list)
    # item_seen = []
    # result_table = [0 for i in range(knapsack_max_weight + 1)]
    # for item in items:
    #     item_seen.append(item)
    #     weight = item[0]
    #     value = item[1]
    #     for weight_limit in range(knapsack_max_weight + 1):
    #         if weight > weight_limit:
    #             continue
    #         elif weight <= weight_limit:
    #             remaining_weight = weight_limit - weight  # You should evaluate the weight of the current item. [YC] This it important to note that the remaining weight should not be calculated with the weight limit of the knapsack, but the current weight limit!!!
    #             if weight not in items_in_bag[remaining_weight]:  # This is important to avoid adding one object twice
    #                 possible_value = value + result_table[remaining_weight]
    #                 bag_elements = items_in_bag[remaining_weight] + [weight] # Now you update the element in the bag, it should contain the current weight and whatever is it in the remaining_weight bag.
    #             else:
    #                 possible_value = max(result_table[remaining_weight], value)
    #                 if value > result_table[remaining_weight]:
    #                     bag_elements = [weight]
    #                 else:
    #                     bag_elements = items_in_bag[remaining_weight] # TODO: This method doesn't include the items that were seen but not in the remaining weight.
    #             if possible_value > result_table[weight_limit]:
    #                 items_in_bag[weight_limit] = bag_elements
    #                 result_table[weight_limit] = possible_value

    # [YC] Yay!!!!!!
    result_table = [[0 for i in range(knapsack_max_weight + 1)] for j in range(len(items) + 1)]  # This is to build a matrix of the result
    for index, item in enumerate(items):
        index += 1  # The first row of the result_table is 0s, when no element is visited
        weight = item[0]
        value = item[1]
        result_table[index] = result_table[index - 1].copy()
        for weight_limit in range(knapsack_max_weight + 1):
            if weight > weight_limit:
                continue
            elif weight <= weight_limit:
                remaining_weight = weight_limit - weight
                possible_value = value + result_table[index - 1][remaining_weight]
                result_table[index][weight_limit] = max(result_table[index][weight_limit], possible_value)

    return result_table[index][knapsack_max_weight]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}
]

for test in tests:
    assert test['correct_output'] == max_value(**test['input'])