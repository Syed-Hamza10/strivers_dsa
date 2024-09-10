def brute(arr, target):
    '''find two index which equals to target'''

    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if arr[i] + arr[j] == target:
                return (i, j)
            
    return -1

print(brute([2,7,9,15], 22))