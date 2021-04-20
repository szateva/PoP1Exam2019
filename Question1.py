""" Implement a function
number_of_differences(n, m, A, B)
that takes two matrices of integers A and B with n rows and m columns and returns a
number of positions (i; j) where an element at this position in A is not equal to the
element at this position in B. You may assume that the matrices are of the correct size
and are specified in a standard way as lists of lists.
Indicative test cases:
assert number_of_differences(2,3, [[1,2,3], [4,5,6]], [[1,2,4],\
[3,5,6]]) == 2
assert number_of_differences(2,2, [[1,2], [3,4]], [[1,2], [3,4]])== 0 """

def number_of_differences(n, m, A, B):
    diff = 0
    for row in range(n):
        for col in range(m):
            if A[row][col] != B[row][col]:
                diff +=1
    return diff
