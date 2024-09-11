def brute(arr):
    maxi = -float('inf')
    n = len(arr)

    for i in range(n):
        sum = 0
        for j in range(i , n):
            sum += arr[j]
            maxi = max(sum, maxi)

    return maxi

print(brute([5,4,-1,7,8]))

def optimal(arr):
    n = len(arr)
    maxi = -float('inf')
    ansStart, ansEnd = -1, -1 #to retun subarray as well
    sum = 0

    if len(arr) == 1:
        return arr[0]
    
    for i in range(n):
        if sum == 0:
            start = i
        sum += arr[i]
        if sum > maxi:
            maxi = sum
            ansStart = start
            ansEnd = i

        if sum < 0:
            sum = 0

    return maxi, ansStart, ansEnd

print(optimal([5,4,-1,7,8]))