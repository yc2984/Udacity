class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """
    stack = Stack()
    minimum = 0  # This is the number of "}" that has to be flipped.
    for bracket in input_string:
        if bracket == "{":
            stack.push(bracket)
        else:
            if not stack.is_empty():
                stack.pop()
            else:
                minimum += 1
                stack.push("{")

    if stack.size() % 2 == 0:  # stack.size()/ 2 is the number of "{" that has to be flipped
        return stack.size() / 2 + minimum
    else:
        return -1


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_3)

test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_4)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_5)

test_case_yang = ["{}}{{{", 3]
test_function(test_case_yang)

