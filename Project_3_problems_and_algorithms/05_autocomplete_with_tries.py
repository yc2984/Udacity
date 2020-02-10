"""Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings.
Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
Give it a try by implementing the TrieNode and Trie classes below!
"""

"""Finding Suffixes
Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. 
To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. 
For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes 
from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

Using the code you wrote for the TrieNode above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)"""


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.children = {}

    def insert(self, char):
        if char not in self.children:
            self.children.update({char: TrieNode(char)})

    def suffix_helper(self, prefix, result=[]):
        if self.is_word:
            result.append(prefix + self.char)
        prefix = prefix + self.char
        for char, child in self.children.items():
            result.extend(child.suffix_helper(prefix, result=[]))
        return result

    def suffixes(self, suffix='', results=[]):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        for char, child in self.children.items():
            results.extend(child.suffix_helper('', result=[]))
        return results


class Trie:
    def __init__(self):
    ## Initialize this Trie (add a root node)
        self.root = TrieNode("")

    ## Add a word to the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True

    ## Find the Trie node that represents this prefix
    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes(results=[])))
        else:
            print(prefix + " not found")
    else:
        print('')

# Test cases:
print('\n test_case_1')
f('fun')  # Expected: ['ction']
print('\n test_case_2')
f('ant')  # Expected: ['hology', 'agonist', 'onym']
print('\n test_case_3')
f('trie')  # Expected: []
print('\n test_case_4')
f('f') # actory, un, unction
print('\n test_case_5')
f('a')  # nt, nthology, ntagonist, ntonym
print('\n test_case_6')
f('')  # []