def brute(arr, d):
    '''d is the number of places to rotate'''
    
    n = len(arr)
    d = d % n

    temp = [0] * d

    for i in range(d):
        temp[i] = arr[i]
    
    for i in range(d,n):
        arr[i - d] = arr[i]

    j = 0
    for i in range(n-d,n):
        arr[i] = temp[j]
        j += 1

    return arr

