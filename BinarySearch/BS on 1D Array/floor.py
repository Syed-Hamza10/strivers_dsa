# largest number in array <= x

def foo(nums, x):
    n  = len(nums)
    left, right = 0, n - 1

    ans = n

    while left <= right:
        mid = left + ( right - left) // 2

        if nums[mid] <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans if x <= max(nums) else -1

print(foo([10,20,30,40,50], 35))