def brute(nums, target):
    ans = []
    n = len(nums)

    for i in range(n):
        required_more = target - nums[i]

        for j in range(i + 1, n):
            if nums[j] == required_more:
                ans.extend([i,j])
                break
    return ans

def optimal(nums, target):
    n = len(nums)

    num_to_index = {} #kiya pehle hamne kabhi wo element dekha hai jo required hai?

    for i in range(n):
        remaining = target - nums[i] 

        if remaining in num_to_index:
            return [num_to_index[remaining], i+1]
        
        num_to_index[nums[i]] = i+1

    
#print(optimal([-1,0], -1))

def optimal2(nums, target): #if we have to return elements,not index
    nums.sort()
    n = len(nums)  
    ans = []

    i = 0
    j = n - 1

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
            ans.extend([nums[i], nums[j]])
            i += 1
            j -= 1
    return ans
print(optimal2([1,7,2,15], 9))