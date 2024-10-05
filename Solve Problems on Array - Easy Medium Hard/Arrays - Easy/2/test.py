def moving_zeros_to_end(nums):
    n = len(nums)

    i = 0
    for x in nums:
        if x != 0:
            i += 1
        else:
            break
    
    for j in range(i+1, n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i +=1
    return nums

print(moving_zeros_to_end([1,0,2,0,3,0,4,0,5]))