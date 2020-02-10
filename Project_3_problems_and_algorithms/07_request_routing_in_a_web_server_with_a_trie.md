**data structure**
I'm using the given data structure.

**time complexity** 

* add_handler has O(n): n = number of parts in the path
    * split_path: O(n)
    * RouteTrie.insert: O(n)
        * For loop O(n)
        * RouteTrieNode.insert O(1)


* lookup: O(n) n = number of parts in the path
    * split_path: O(n)
    * RouteTrie.find: O(n)
        * For loop O(n)
     
* split_path: O(n) n = number of parts in the path



**space complexity**

* add_handler has O(k + n): n = number of parts in the path, k = number of nodes in the RouteTrie
    * split_path: O(n)
    * RouteTrie.insert: O(k + n)
        * RouteTrieNode.insert O(k + n): worst case all the nodes in the trie are the children of this node and in addition you need to hold the parts in the path. 


* lookup: O(k + n) n = number of parts in the path, k = number of nodes in the RouteTrie
    * split_path: O(n)
    * RouteTrie.find: O(k + n): worst case all the nodes in the trie are the children of this node and in addition you need to hold the parts in the path. 
     
* split_path: O(n) n = number of parts in the path

