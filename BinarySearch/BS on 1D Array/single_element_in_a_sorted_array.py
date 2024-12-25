def foo(nums):

    n = len(nums)

    left = 0
    right = n - 1

    if n == 1:
        return nums[0]

    while left < right:
        mid = left + (right - left)//2

        isEven = True if (right - mid) % 2 == 0 else False

        
        if nums[mid] == nums[mid + 1]:
            if isEven:
                left = mid + 2 #go right
            else:
                right = mid - 1
        else:
            if isEven:
                right = mid
            else:
                left = mid + 1
    return nums[right] 
                

print(foo([1,1,2,2,3,4,4,8,8]))