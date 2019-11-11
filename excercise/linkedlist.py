class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """

        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = self.head
        print("After prepending %s, self.head.value %s, self.tail.value %s", value, self.head.value, self.tail.value)

    def append(self, value):
        """ Append a value to the end of the list. """

        new_node = Node(value)
        if self.head is None:
            print("Appending first element")
            self.head = Node(value)
            self.tail = self.head
            return

        self.tail.next = new_node  # todo: why the self.head also changed in this step, because they are both pointing to the same node
        self.tail = new_node  # todo: why here only self.tail becomes new_node, self.head still stays the same

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """

        if not self.head:
            return None
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

    def remove(self, value):
        """ Remove first occurrence of value. """

        print("Before removing %s", self.to_list())
        if not self.head:  # Nothing to be removed
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                if current_node.next is None:
                    self.tail = current_node
                return
            current_node = current_node.next

    def pop(self):
        """ Return the first node's value and remove it from the list. """

        if not self.head:
            return None
        value = self.head.value
        self.remove(value)
        return value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """

        if not self.head or pos == 0:
            self.prepend(value)
            return

        new_node = Node(value)
        current_pos = 1
        current_node = self.head

        while current_node:
            if pos == current_pos:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_pos += 1
            current_node = current_node.next
        self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"