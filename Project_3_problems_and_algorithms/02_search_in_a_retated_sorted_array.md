**data structure**
I used binary search to solve this problem because by modifying the standard binary search algorithm, we can still know which side to recurse the function on, so that to maintain the runtime of log n.
**time complexity**
O(log(n)), n is the length of the list. The max height of the binary search tree is log(n). 
**space complexity**
O(n), the space it takes is always the same than the length of input_list

