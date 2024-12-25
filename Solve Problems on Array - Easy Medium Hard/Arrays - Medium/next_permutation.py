def brute(nums):
    '''thorugh recrusion, generate all permutations, store them.
    then find the next permutation through linear search.
    TC will be N! x N, so let's not do it'''
    return


def optimal(nums):
    '''Algo ke 3 steps hai
    1. Right se start kro, jese hi pehla index mile jo pichle wale se chota ho, store krlo
    example, when i + 1 > i
    2. is index ke right per dekho, pehla element which is just greater than this.
    3. in dono ko apas me swap krlo, or right side ko reverse krdo'''

    idx = None
    n = len(nums)
    for i in range(n - 2, -1, -1): # going till 0th index, find someone smaller than i + 1
        if nums[i] < nums[i + 1]:
            idx = i
            break

    if idx is None:
        nums =  reversed(nums) #agar next permutation hai hi nahi, mtlb 3 2 1 se 1 2 3 aye ga
        return
    for i in range(n - 1, idx, -1):
        if nums[i] > nums[idx]:
            nums[i], nums[idx] = nums[idx], nums[i] #looking at right, swapping the first index which is just greater than idx
            break

    nums[idx + 1:] = reversed(nums[idx + 1:])
    return nums

print(optimal([3,2,1]))
