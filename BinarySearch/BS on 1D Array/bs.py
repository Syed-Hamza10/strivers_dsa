def search(nums, target):
    n = len(nums)

    low = 0
    high = n - 1

    #mid = (low + high) // 2 gives TLE when INT_MAX is reached
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(search([-1,0,3,5,9,12], 9))