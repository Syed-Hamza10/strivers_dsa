def brute(nums, k):
    n = len(nums)
    cnt = 0
    for start in range(n):
        sum = 0
        for end in range( start, n):
            sum += nums[end]
            if sum == k:
                cnt += 1
    return cnt

print(brute([1,1,1], 2))

def optimal(nums, k):
    '''kiya past me sum dekha tha? ye intution hai'''
    
    hash = {0 : 1} #prefix sum in the start is 0. it is used to handle cases like [1,-1] , k = 0
    prefix = 0
    n = len(nums)
    count = 0

    for i in range(n):
        prefix += nums[i]
        if (prefix - k) in hash:
            count += hash[prefix - k]
        if prefix in hash:
            hash[prefix] += 1
        else:
            hash[prefix] = 1

    return count

print(optimal([1,2,3], 3))

        