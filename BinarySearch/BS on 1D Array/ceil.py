# find smallest index greater than equal to x - also called ceil

def foo(nums, x):
    n = len(nums)

    low, high = 0, n -1
    ans= n

    while low <= high:
        mid = low + ( high - low) // 2

        if nums[mid] >= x: #it could be the solution    
            ans = mid
            high = mid - 1 # look for smaller index on the left
        else:
            low = mid + 1
    return ans if ans != n else -1

print(foo([1,2,3,3,5,8,8,10,10,11], 11))