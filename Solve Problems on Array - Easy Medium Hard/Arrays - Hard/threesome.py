res = []

def twoSum(nums, target, i , j): #if we have to return elements,not index

    global res

    while i < j:
        if nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            while i < j and nums[i] == nums[i + 1]:
                i += 1
            while i < j and nums[j] == nums[j - 1]:
                j -= 1
            res.append([-target, nums[i], nums[j]])
            i += 1
            j -= 1
def threeSum(nums):
    global res

    res.clear()
    nums.sort()

    n = len(nums)

    if n < 3:
        return []

    

    for i in range(n):
        if i !=0 and nums[i] == nums[i - 1]: # to check for duplicate value
            continue
        n1 = nums[i]
        target = -n1
        twoSum(nums, target, i + 1, n-1) 
    return res



print(threeSum([0,1,1]))