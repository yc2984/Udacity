class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


def add_recursive(word, index, result):
    """

    :param word:
    :param index:
    :param result: dict
    :return:
    """
    if index == len(word) - 1:
        result[word[index]] = {"word_end": True}
        return result
    else:
        result[word[index]] = add_recursive(word, index + 1, result)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        if len('word') < 1:
            return
        return add_recursive(word, 0, {})

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node:
                return False

            current_node = current_node[char]

        return current_node['word_end']


word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
