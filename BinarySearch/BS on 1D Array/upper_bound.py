# smallest element greater than x

def foo(nums, x):
    n = len(nums)

    left, right = 0, n-1

    ans = n
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > x:
            ans = mid
            right = mid - 1 # look for smaller index on the left
        else:
            left = mid + 1
    return ans if ans != n else -1

print(foo([1,2,3,3,5,8,8,10,10,11], 10))