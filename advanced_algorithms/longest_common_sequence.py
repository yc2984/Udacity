"""In text analysis, it is often useful to compare the similarity of two texts (imagine if you were trying to determine plagiarism between a source and answer text).
 In this notebook, we'll explore one measure of text similarity, the Longest Common Subsequence or LCS.

The Longest Common Subsequence is the longest string of letters that are the same between to strings.

A short example:

For two input strings, A and B
A = 'ABCD'
B = 'BD'
The LCS is 'BD', which has a length of 2 characters"""

def lcs(string_a, string_b): # [YC] Yay!!

    matrix = [[0] * (len(string_b) + 1) for i in range(len(string_a) + 1)]
    for j in range(len(string_b)):
        for i in range(len(string_a)):
            if string_a[i] == string_b[j]:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
            else:
                matrix[i + 1][j + 1] = max(matrix[i][j + 1], matrix[i + 1][j])
    return matrix[len(string_a)][len(string_b)]

## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')


# Complexity
# n * m, n is the lenght of the first string, and m is the length of the second string.

# Solution TODO: why? N ^ 2??
"""# The time complexity of the above implementation
# is dominated by the two nested loops,
# which give us an O(N^2) time complexity."""