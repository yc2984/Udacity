**data structure**
I'm using the given data structure.

**time complexity** 

* add_handler has O(k * n): n = number of parts in the path, k = number of nodes in the RouteTrie
    * split_path: O(n)
    * RouteTrie.insert: O(k * n)
        * For loop O(n)
        * RouteTrie.find_part_in_children: O(k)
        * RouteTrieNode.insert: worst case all the nodes in the trie are the children of this node: O(k)


* lookup: O(k * n) n = number of parts in the path, k = number of nodes in the RouteTrie
    * split_path: O(n)
    * RouteTrie.find: O(n * k)
        * For loop O(n)
        * node.find_part_in_children: O(k)
     
* split_path: O(n) n = number of parts in the path




**space complexity**

* add_handler has O(k + n): n = number of parts in the path, k = number of nodes in the RouteTrie
    * split_path: O(n)
    * RouteTrie.insert: O(k + n)
        * RouteTrie.find_part_in_children: O(k)
        * RouteTrieNode.insert: worst case all the nodes in the trie are the children of this node: O(k)


* lookup: O(k + n) n = number of parts in the path, k = number of nodes in the RouteTrie
    * split_path: O(n)
    * RouteTrie.find: O(k + n)
        * node.find_part_in_children: O(k): worst case all the nodes in the trie are the children of this node: O(k)
     
* split_path: O(n) n = number of parts in the path

