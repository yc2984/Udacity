# this code makes the tree that we'll traverse

class Node(object):

    def __init__(self, value=None):
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


from collections import deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
    can use a for loop (try one or both ways)
    """
    def insert_with_loop(self, new_value): # [YC] yay!
        current_node = self.get_root()
        if not current_node:
            self.set_root(new_value)
            return
        new_node = Node(new_value)
        while True:
            print("new_value %s, current_node value %s", new_value, current_node.get_value())
            if new_value == current_node.get_value():
                break
            if new_value > current_node.get_value():
                if current_node.has_right_child():
                    current_node = current_node.get_right_child()
                else:
                    current_node.set_right_child(new_node)
                    break
            if new_value < current_node.get_value():
                if current_node.has_left_child():
                    current_node = current_node.get_left_child()
                else:
                    current_node.set_left_child(new_node)
                    break

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def insert_with_recursion(self, new_value): # [YC] yay!

        current_node = self.get_root()
        if not current_node:
            self.set_root(new_value)
            return
        new_node = Node(new_value)

        def insert_node(new_value, current_node):
            current_value = current_node.get_value()
            # when new_value < current_value, insert as left child, if left child doesn't exist, otherwise call insert_node on the left child
            if new_value < current_value:
                if current_node.has_left_child():
                    insert_node(new_value, current_node.get_left_child())
                else:
                    current_node.set_left_child(new_node)
                    return

            if new_value > current_value:
                if current_node.has_right_child():
                    insert_node(new_value, current_node.get_right_child())
                else:
                    current_node.set_right_child(new_node)
                    return

        return insert_node(new_value, current_node)

    def search(self, value):  # [YC] yay!
        if not self.get_root():
            return False
        current_node = self.get_root()
        new_node = Node(value)
        while True:

            comparison = self.compare(current_node, new_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if current_node.has_left_child():
                    current_node = current_node.get_left_child()
                else:
                    return False
            elif comparison == 1:
                if current_node.has_right_child():
                    current_node = current_node.get_right_child()
                else:
                    return False

    def delete(self, value):
        if not self.get_root():
            return
        root_node = self.get_root()
        new_node = Node(value)

        comparison = self.compare(root_node, new_node)

        if comparison == 0:  # It means the node is the be deleted. So now we need to find the succesor to the node.
            if not root_node.has_left_child() and not root_node.has_right_child():
                return
            if root_node.has_left_child() and not root_node.has_right_child():
                self.root = root_node.get_left_child()
                return
            if root_node.has_right_child() and not root_node.has_left_child():
                self.root = root_node.get_right_child()
                return
            if root_node.has_right_child() and root_node.has_left_child():  # find the next value that is bigger than root
                current_node = root_node.get_right_child()
                # Find the last left node of the right node.
                while current_node.has_left_child():
                    left_node = current_node.get_left_child()
                if left_node.has_right_child():   # [YC] how to you find the parent of the left_node that becomes the new root???
                    self.root = left_node



        elif comparison == -1:
            if current_node.has_left_child():
                current_node = current_node.get_left_child()
            else:
                return False
        elif comparison == 1:
            if current_node.has_right_child():
                current_node = current_node.get_right_child()
            else:
                return False


    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s

tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5) # insert duplicate
print(tree)

tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
print(tree)


print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
""")
print(tree)

tree = Tree()
tree.delete(5)
print(tree)