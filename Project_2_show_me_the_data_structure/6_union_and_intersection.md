
I chose set because it's easy to check if an element is in the set, the underlying data structure: 
doubly linked list with a hashtable makes it take constant time for value look up and insert. 


time complexity union: 	O(s + t)
    - The worse case is that both of the linkedlist have unique elements, we need to go through every one of them

space complexity union: O(len(s)+len(t))
    - The worse case is that both of the linkedlist have unique elements, we need to go through every one of them, so the result_list will have the size of len(s)+len(t)


time complexity intersection: O(s + t)
    - lookup takes O(1) in sets so the slowest operation here would be converting the linked lists to sets and that 
    will take O(s + t) as we need to go through every element i both of the lists.

space complexity intersection: O(s + t)
    - The worse case is that both of the linkedlist have unique elements, we need to go through every one of them, 
    so the result_list will have the size of s + t. And in the meantime, we need to keep the two input lists in memory,
    so even if the results are empty, the input lists take space. 
