import sys
import operator
from collections import deque

class Node:
    def __init__(self, freq, char=None):
        self.char = char
        self.freq = freq
        self.code = None
        self.left = None
        self.right = None

class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, node):
        # insert element at the next index
        self.cbt[self.next_index] = node

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element.freq > child_element.freq:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = parent if parent.freq <= left_child.freq else left_child

            # compare with right child
            if right_child is not None:
                min_element = right_child if right_child.freq < min_element.freq else min_element

            # check if parent is rightly placed
            if min_element.freq == parent.freq:
                return

            if min_element.freq == left_child.freq:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]


def get_freq_tuple_list(data):
    """
    :param data(str):
    :return: List(tuple)
    """

    # Find the frequency of each letter
    freq_dict = {}
    for letter in data:
        if letter not in freq_dict:
            freq_dict[letter] = 1
        else:
            freq_dict[letter] += 1
    print(freq_dict)
    return freq_dict


def create_heap(data):

    freq_dict = get_freq_tuple_list(data)
    heap = Heap()
    for char, freq in freq_dict.items():
        node = Node(char=char, freq=freq)
        heap.insert(node)
    return heap


def huffman_encoding(data):
    heap = create_heap(data)
    while heap.size() > 1:

        # Find the two character with the least frequency
        right = heap.remove()
        left = heap.remove()
        new_freq = left.freq + right.freq
        new_node = Node(freq=new_freq)
        heap.insert(new_node)
        new_node.left = left
        new_node.right = right

    huffman_dict = {}
    node = heap.cbt[0]
    node.code = ''  # THe head node doesn't need to have any code.

    def traverse(node, huffman_dict):
        # Assign zero to all the right node, and assign one to all the left node
        if node.left:
            node.left.code = '{}0'.format(node.code)
            if node.left.char:
                huffman_dict[node.left.char] = node.left.code
            traverse(node.left, huffman_dict)

        if node.right:
            node.right.code = '{}1'.format(node.code)
            if node.right.char:
                huffman_dict[node.right.char] = node.right.code
            traverse(node.right, huffman_dict)

    traverse(node, huffman_dict)

    coding = ''
    for char in data:
        coding += huffman_dict[char]

    return coding, node


def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))