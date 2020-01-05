"""Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    node_1 = llist_1.head
    node_2 = llist_2.head
    unique_values = set()

    while node_1:
        unique_values.add(node_1.value)
        node_1 = node_1.next

    while node_2:
        unique_values.add(node_2.value)
        node_2 = node_2.next

    result_list = LinkedList()
    for value in unique_values:
        result_list.append(value)
    return result_list


def intersection(llist_1, llist_2):
    node_1 = llist_1.head
    unique_values_1 = set()

    while node_1:
        unique_values_1.add(node_1.value)
        node_1 = node_1.next

    node_2 = llist_2.head
    unique_values_2 = set()
    while node_2:
        unique_values_2.add(node_2.value)
        node_2 = node_2.next

    unique_values = unique_values_1.intersection(unique_values_2)
    result_list = LinkedList()
    for value in unique_values:
        result_list.append(value)

    return result_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# Expected: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2))
# Expected: 4 -> 21 -> 6 ->


# Test case 2: no intersection

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# Expected: 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print (intersection(linked_list_3,linked_list_4))
# Expected: empty

# Test case 3: empty list

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# Expected : 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_5,linked_list_6))
# Expected: empty