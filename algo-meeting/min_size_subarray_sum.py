'''Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''

def optimal(nums, target):

    i = 0
    total = 0
    n = len(nums)
    res = n + 1
    for j in range(n):
        total += nums[j]

        while total >= target:
            res = min(res, j - i + 1)
            total -= nums[i]
            i += 1
    return 0 if res > n else res

def brute(nums, target):
    total = 0
    n = len(nums)
    res = n + 1

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum >= target:
                res = min(res, j - i + 1)
                break    
            
    return 0 if res == n + 1 else res    
            

print(brute([2,3,1,2,4,3], 7))
        
