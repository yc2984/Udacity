import sys
import operator
from collections import deque

class Node(object):

    def __init__(self,  key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


def get_freq_tuple_list(data):
    """
    :param data(str):
    :return: List(tuple)
    """

    # Find the frequency of each letter
    freq = {}
    for letter in data:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1
    print(type(freq.items()))
    # a queue of tuples with the letter as the first element and frequency as the second element
    order_freq = deque(sorted(freq.items(), key=operator.itemgetter(1)))
    return order_freq


def sort_queue_tuple(queue_of_tuple):
    return deque(sorted(queue_of_tuple, key=operator.itemgetter(1)))


def create_huffman_tree(data):

    order_freq = get_freq_tuple_list(data)

    new_value = order_freq[0][1] + order_freq[1][1]
    root = Node(value=new_value)  # The root of the tree
    root.left = Node(key=order_freq[0][0], value=order_freq[0][1])
    root.right = Node(key=order_freq[1][0], value=order_freq[1][1])
    order_freq.popleft()
    order_freq.popleft()

    while len(order_freq) >= 2:
        order_freq.append(root)

        order_freq = sort_queue_tuple(order_freq)
    else:
        return root



def huffman_encoding(data):
    pass


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