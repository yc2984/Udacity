"""In this notebook, you'll be tasked with finding the length of the Longest Palindromic Subsequence (LPS) given a string of characters.

As an example:

With an input string, ABBDBCACB
The LPS is BCACB, which has length = 5
In this notebook, we'll focus on finding an optimal solution to the LPS task, using dynamic programming.
There will be some similarities to the Longest Common Subsequence (LCS) task, which is outlined in detail in a previous notebook.
It is recommended that you start with that notebook before trying out this task.

Hint
Storing pre-computed values

The LPS algorithm depends on looking at one string and comparing letters to one another.
Similar to how you compared two strings in the LCS (Longest Common Subsequence) task,
you can compare the characters in just one string with one another, using a matrix to store the results of matching characters.

For a string on length n characters, you can create an n x n matrix to store the solution to subproblems.
In this case, the subproblem is the length of the longest palindromic subsequence, up to a certain point in the string (up to the end of a certain substring).

It may be helpful to try filling up a matrix on paper before you start your code solution.
If you get stuck with this task, you may look at some example matrices below (see the section titled Example matrices), before consulting the complete solution code."""


def lps(input_string):
    # [YC] Yay!! # TODO: questions, what is the test result for 'ab', it should be zero, not 1, right?
    # The function should return one value: the LPS length for the given input string
    string_a = input_string
    string_b = input_string[::-1]
    matrix = [[0] * (len(input_string) + 1) for _ in range(len(input_string) + 1)]
    for i in range(len(string_a)):
        for j in range(len(string_b)):
            if string_a[i] == string_b[j]:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
            else:
                matrix[i + 1][j + 1] = max(matrix[i + 1][j], matrix[i][j + 1])
    return matrix[len(string_a)][len(string_b)]


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)

string = 'BANANA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

# TODO: Think about this edge case
string = 'AB'
solution = 0
test_case = [string, solution]
test_function(test_case)