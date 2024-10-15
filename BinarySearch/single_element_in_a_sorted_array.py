def foo(nums):

    left = 0
    right = len(nums) - 1
    n = len(nums)

    while left <= right:
        mid = left + (right - left)//2

        if (n - 1 - mid) % 2 == 0: #mtlb right side per even numbers are left
            if nums[mid + 1] == nums[mid]:
                left = mid + 1 #go left
            else:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]
                right = mid - 1 #go right
        else: #odd
            if nums[mid + 1] == nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return nums[mid] 
                

print(foo([1,1,2,2,3,4,4,8,8]))