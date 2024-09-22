def brute(matrix):
    '''
    1 2 3       7 4 1
    4 5 6       8 5 2
    7 8 9       9 6 3
    
     Take another dummy matrix of n*n, and
     then take the first row of the matrix and put it in the last column of the dummy matrix, 
     take the second row of the matrix, and put it in the second last column of the matrix and so.
    [0][0] = [0][2]
    [0][1] = [1][2]
    [0][2] = [2][2]
    
    matrix[i][j] = rotated[j][n-1-i]'''

    n = len(matrix)

    rotated = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
    #print(rotated)


def optimal(matrix):
    '''approach is to take the transpose first, then reverse every row.'''
    n = len(matrix)
    def transpose(matrix):
        nonlocal n
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    transpose(matrix)
    '''4. for j in range(i):
This loop ensures that only the elements below the diagonal are swapped.
The idea is that swapping happens for
matrix[i][j] and matrix[j][i] only when i > j, i.e., below the diagonal.
This avoids double-swapping and keeps the diagonal elements intact.'''
    for i in range(n):
        matrix[i].reverse()
    #print(matrix)
    
optimal([[1,2,3],[4,5,6],[7,8,9]])