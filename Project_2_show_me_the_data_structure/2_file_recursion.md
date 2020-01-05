### Design:
The data structure is a tree where files act as leaves and directories act as internal nodes. I choose to use array 
to represent the tree. 

n = number of files (k) + number of directories (x)

### Time Complexity:
The time complexity is O(n) because we have to traverse through all the element (files and directories) in the path.

### Space Complexity:
The space complexity is O(n) because the worse case scenario would be: there is only one directory inside each of the 
directory and no files until the deepest directory, which contains all k number of files. So we will need to hold x 
stacks and k files at the same time k + x = n. 