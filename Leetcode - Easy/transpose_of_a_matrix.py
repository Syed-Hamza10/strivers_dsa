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
    '''* is called splat operator and it unpacks the rows, gives them separately to zip function'''


def transpose_of_square_matrix(matrix):
    ROW = len(matrix)
    COL = len(matrix[0])

    for r in range(ROW):
        for c in range(r + 1, COL):
            matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]

    return matrix