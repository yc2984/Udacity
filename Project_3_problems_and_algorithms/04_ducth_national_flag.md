**data structure**
This problem requires to sort the array in single traversal. Since there are only 3 values in the array, then we can 
keep moving the zeros to the front while moving the twos to the back, and keep ones in their place, then when we finish traversing, the array should be sorted.
**time complexity** 
O(n), n is the lenght of the array. Because we only traverse once every element. 
**space complexity**
O(n), we only need to hold the same size than the input list. 