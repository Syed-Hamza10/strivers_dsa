def brute(arr, target):
    '''find two index which equals to target'''

    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if arr[i] + arr[j] == target:
                return (i, j)
            
    return -1

print(brute([2,7,9,15], 22))


def optimal(arr, target):
    num_to_index = {} #hash to store whether we've seen the remaining sum previously or not
    n = len(arr)

    for i in range(n):
        remaining = target - arr[i]
        if remaining in num_to_index:
            return [num_to_index[remaining], i]
        
        num_to_index[arr[i]] = i

print(optimal([2,7,9,15], 22))