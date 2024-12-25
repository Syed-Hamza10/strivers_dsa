def foo(matrix, target):

    m = len(matrix)
    n = len(matrix[0])

    i = 0
    j = n - 1

    while i < m and j > -1:
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            return True
    return False

print(foo([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
     