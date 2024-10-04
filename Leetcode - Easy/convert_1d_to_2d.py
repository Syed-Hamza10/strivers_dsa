def approach(original,m, n):
    if len(original) != m*n:
        return []
    
    result = [[0 for _ in range(n)] for _ in range(m)]

    idx = 0
    for row in range(m):
        for col in range(n):
            result[row][col] = original[idx]
            idx += 1
    return result


def approach(original,m, n):
    if len(original) != m*n:
        return []
    
    result = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(len(original)):
        row = i // n
        col= i % m
        result[row][col] = original[i]
    return result


