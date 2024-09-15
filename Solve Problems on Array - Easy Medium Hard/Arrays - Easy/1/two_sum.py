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

    
print(optimal([-1,0], -1))
