The data structure needed for this problem is the one that can be fast sorted or can find the minimum in fast, because we need to constantly get the minimum of the frequency. At first I tried to use a list, but it was not optimal because the time complexity will be n^2, because when adding every element of the huffman tree, we need to sort the tree at O(n). Then my mentor suggested me to study the heap data structure in the next chapter, because it's a priority queue so that you can easily pop the max or the min and insert at O(log(n)), which is ideal for this problem. 

**time complexity** of **huffman_encoding**: O(nlog(n)):
    - `get_freq_tuple_list` has O(n)
    - `create_heap` has O(n)
    - `heap.insert` has O(log(n))
    - `heap.remove` has O(log(n))
    - while loop contains heap.insert and heap.remove which makes it O(nlog(n))
    - `traverse` function has O(n)
    -  for loop has O(n)   

**space complexity** of **huffman_encoding**: O(n):
    - `get_freq_tuple_list` has O(n)
    - `create_heap` has O(n)
    - `heap.insert` has O(n)
    - `heap.remove` has O(n)
    - `traverse` function has O(n). The max number of the stacks in memory is log(n). The huffman_dict can be the same size than the number of characters. 
    -  for loop has O(1)  
    
    
**time complexity** of huffman_decoding: O(log(n)):
    - traversing a complete binary tree takes O(log(n)), because the max height of the tree if log(n). 
    
**space complexity** of huffman_decoding: O(n):
    - we need to keep the entire data in memory all the time. 
    

