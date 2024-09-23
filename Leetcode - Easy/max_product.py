def foo(nums):
    
    first_max = nums[0]
    sec_max = -1
    n = len(nums)

    for i in range(1, n):
        if nums[i] > first_max:
            sec_max = first_max
            first_max = nums[i]
        if nums[i] < first_max and nums[i] > sec_max:
            sec_max = nums[i]
    return (first_max - 1) * (sec_max - 1)
    
#print(foo([3,4,5,2]))

def maxProduct(nums):
    cur_max = nums[0]
    result = 0
    for num in nums:
        result = max(result, (num-1) * (cur_max-1))
        cur_max = max(cur_max, num)
    return result

print(maxProduct([3,4,6,2,5]))