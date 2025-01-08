def brute(nums):
    '''element jiske right per use koi bara na ho, wo leader hai'''

    #maxi = -float('inf')
    n = len(nums)
    ans = []

    for i in range(n):
        isLeader = True
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                isLeader = False
                break
        if isLeader:
            ans.append(nums[i])
    return ans

def optimal(arr):
    n = len(arr)
    maxi = -float('inf')
    ans = []
    for i in range(n-1, -1, -1):
        if arr[i] > maxi:
            ans.append(arr[i])
            maxi = arr[i]
    return list(reversed(ans))
print(optimal([16,17,4,3,5,2]))