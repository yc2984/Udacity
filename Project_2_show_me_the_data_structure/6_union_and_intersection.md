
I chose set because it's easy to check if an element is in the set, average takes O(1) and worse case O(n)


time complexity union: 	O(len(s)+len(t))
    - The worse case is that both of the linkedlist have unique elements, we need to go through every one of them

space complexity union: O(len(s)+len(t))
    - The worse case is that both of the linkedlist have unique elements, we need to go through every one of them, so the result_list will have the size of len(s)+len(t)


time complexity intersection: O(len(s) * len(t))
    - worse case is there is no intersection, so for every element in first linkedlist, we need to go over every element in the second linkedlist. 


space complexity intersection: O(len(s)+len(t))
    - The worse case is that both of the linkedlist have unique elements, we need to go through every one of them, so the result_list will have the size of len(s)+len(t)
