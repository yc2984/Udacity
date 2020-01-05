I chose recursion to deal with this problem because it's the most logical way to check membership in a hierarchical way. 

n = the sum of number of groups (k) and users (x) 

time complexity O(n)
    - The worse case would be: only one group (it's in the deepest sub group) contain users, all the other groups are empty. And the user we are looking for is the last user of that group. So we need to check all the empty groups and go through all teh users. 
    
space complexity O(n)
    - the worse case scenario would be: there is only one group inside each of the 
group and no users until the deepest group, which contains all k number of users. So we will need to hold k
stacks and x users at the same time, so it takes k + x = n. 