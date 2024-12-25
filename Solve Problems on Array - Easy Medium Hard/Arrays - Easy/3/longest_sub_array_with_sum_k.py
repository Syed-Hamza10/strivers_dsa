def brute(arr, k):
    n = len(arr)
    
    maxLen = 0
    for i in range(n):
        for j in range(i, n):
            if sum(arr[i : j+1]) == k:
                maxLen = max(len(arr[i: j + 1]), maxLen)
    return maxLen


def better(arr, k): #only work for +ves and zeros O(2 * N)
    mySum = arr[0]
    maxLen = 0
    n = len(arr)

    left = right = 0

    while  right < n:
        while left <= right and mySum > k:
            mySum -= arr[left]
            left += 1

        if mySum == k:
            maxLen = max(maxLen, right - left + 1)

        right += 1

        if right < n:
            mySum += arr[right]

    return maxLen    




print(brute([2,3,5,1,9], 20))