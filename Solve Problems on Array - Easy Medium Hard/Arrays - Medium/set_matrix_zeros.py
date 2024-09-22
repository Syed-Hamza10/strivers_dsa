# https://leetcode.com/problems/set-matrix-zeroes/description/

def brute(matrix):
    '''
    First, we will use two loops(nested loops) to traverse all the cells of the matrix.
    If any cell (i,j) contains the value 0, we will mark all cells in row i and column j with None except those which contain 0.
    We will perform step 2 for every cell containing 0.
    Finally, we will mark all the cells containing None with 0.
    Thus the given matrix will be modified according to the question.'''

    '''Time Complexity: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
    Reason: Firstly, we are traversing the matrix to find the cells with the value 0. It takes O(N*M). Now, whenever we find any such cell we mark that row and column with -1. This process takes O(N+M). So, combining this the whole process, finding and marking, takes O((N*M)*(N + M)).
    Another O(N*M) is taken to mark all the cells with -1 as 0 finally.'''

    n, m = len(matrix), len(matrix[0])
    
    def markRow(matrix, n, m , i):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

    def markCol(matrix, n, m , j):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix,n,m,i)
                markCol(matrix,n,m,j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0


def better(matrix):
    n, m = len(matrix), len(matrix[0])

    row, col = [0] * n, [0] * m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = col[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

    '''In the previous approach, we were marking the cells with -1 while traversing the matrix. But in this approach,
      we are not marking the entire row and column instead, we are marking the ith index of row array
      i.e. row[i], and jth index of col array i.e. col[j] with 1. These marked indices of the two arrays, row and col 
    will tell us for which rows and columns we need to change the values to 0. For any cell (i, j),
      if the row[i] or col[j] is marked with 1, we will change the value of cell(i, j) to 0.'''
    

    '''Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

Space Complexity: O(N) + O(M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: O(N) is for using the row array and O(M) is for using the col array.'''
