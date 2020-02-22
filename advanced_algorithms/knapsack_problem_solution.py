
import collections

Item = collections.namedtuple('Item', ['weight', 'value'])

def max_value(knapsack_max_weight, items):
    lookup_table = [0] * (knapsack_max_weight + 1)

    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value) # Note [YC] This is okay and you don't need to worry about repeated element because you are counting backwards, the value of lookup_table[capacity - item.weight] was still not updated, so it's from the last row, just like my solution. 

    return lookup_table[-1]



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