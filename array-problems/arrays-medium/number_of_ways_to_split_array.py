def waysToSplitArray(nums) -> int:
    cur_sum = 0
    res = 0

    for i in range(len(nums) - 1):
        cur_sum = sum(nums[:i+1])
        temp = 0
        for j in range(i + 1, len(nums)):
            temp += nums[j]
        
        if cur_sum >= temp:
            res += 1
    
    return res

print(waysToSplitArray([10,4,-8,7]))