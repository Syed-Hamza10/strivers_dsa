def brute(nums, target):
    ans = []
    n = len(nums)

    for i in range(n):
        temp = target - nums[i]

        for j in range(i + 1, n):
            if nums[j] == temp:
                ans.extend([i,j])
                break
    return ans

def optimal(nums, target):
    n = len(nums)

    num_to_index = {}

    for i in range(n):
        remaining = target - nums[i] 

        if remaining in num_to_index:
            return [num_to_index[remaining], i+1]
        
        num_to_index[nums[i]] = i+1

    
print(optimal([-1,0], -1))
