def foo(matrix):
    n = len(matrix)
    m = len(matrix[0])

    row = [0] * n
    col= [0] * m
    count = 0
 
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:
                row[r], col[c] = row[r] + 1, col[c] + 1
       
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:
                if row[r] == 1 and col[c] == 1:
                    count += 1
    return count

print(foo([[1,0,0],[0,1,0],[0,0,1]]))