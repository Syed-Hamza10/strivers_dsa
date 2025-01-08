'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.'''

def brute(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        ele = arr[i]
        for j in range(n):
            if arr[j] == ele:
                count += 1
        if count > n//2:
            return ele
        
        count = 0

def better(nums):
    hash = {}
    n = len(nums)

    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    
    for key, ele in hash.items():
        if ele > n // 2:
            return key
        
def optimal(nums):
    '''called Boyer-Moore algo, the element apearing more than half length will always cancel out the others'''
    
    res, count = 0, 0
    for num in nums:
        if count == 0:
            res = num
        count += (1 if num == res else -1)

    return res
print(better([8,8,7,7,7]))