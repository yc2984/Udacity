**data structure**
The data structure is Trie.

**time complexity** 

Insert and find costs O(k). k = length of the word that needs to be inserted or searched. Because we need to loop 
over every character in the word, and the insert operation of the TrieNode has O(1).

suffixes method: O(n), n = number of nodes in the Trie. Because we need to go through every nodes in the trie to find
all the suffixes. 

**space complexity**
Insert method:  O(k): In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie. We have to add k new nodes, which takes us O(k) space

Find method: O(1): The space required doesn't change, we only need to hold the current 26 children nodes. 

Suffixes method: O(n): n is the number of words in the trie. The worse case is that every nodes has is_word=True. 

