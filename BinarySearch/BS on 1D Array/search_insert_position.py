def foo(nums, x):
    '''Problem Statement: You are given a sorted array arr of distinct values and a target value x.
      You need to search for the index of the target value in the array.

If the value is present in the array, then return its index. Otherwise, 
determine the index where it would be inserted in the array while maintaining the sorted order.'''
    n = len(nums)
    low, high = 0, n - 1
    ans = n
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] >= x:
            ans = mid
            high = mid - 1 #look for smaller on the right
        else:
            low = mid + 1
    return ans 

print(foo([1,2,4,7],8))