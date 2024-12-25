def brute(nums, k):
    n = len(nums)
    count = 0
    i , j = 0, 1

    while i < n and j < n:
        if sum(nums[i : j + 1]) == k:
            count += 1
            i += 1
            j += 1
        elif sum(nums[i : j + 1]) != k:
            j += 1
    return count
print(brute([1,1,1, 2, 3], 3))