def foo(nums):        
    n = len(nums)

    i , j = 0 , 1
    while j < n:
        if nums[i] == nums[j]:
            j += 1
        elif nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j] , nums[i]
            j += 1
    return i + 1

print(foo([1,2,3,1,4,3,4]))