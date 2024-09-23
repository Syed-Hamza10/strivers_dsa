def foo(matrix):
    ROW = len(matrix)
    COL = len(matrix[0])

    res = [[0 for _ in range(ROW)]for _ in range(COL)]

    for r in range(ROW):
        for c in range(COL):
            res[c][r] = matrix[r][c]
    return res
foo([[1,2,3],[4,5,6],[7,8,9]])

def shortcut(matrix):
    
    return zip(*matrix)
    return list(map(list, zip(*matrix)))
    return [list(row) for row in zip(*matrix)]
    ''' * is called splat operator and it unpacks the rows, gives them separately to zip function'''


def transpose_of_square_matrix(matrix):
    '''just swap the vaues above the diagonal with below the diagonal'''
    ROW = len(matrix)
    COL = len(matrix[0])

    for r in range(ROW):
        for c in range(r + 1, COL):
            matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]

    return matrix

a = list(shortcut([[1,2,3],[4,5,6],[7,8,9]])) 
print([list(i) for i in a])

print(shortcut([[1,2,3],[4,5,6],[7,8,9]]))