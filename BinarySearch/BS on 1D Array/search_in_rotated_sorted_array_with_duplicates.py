def foo(nums, target):

    n = len(nums)

    left, right = 0 , n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True
        
        #edge case
        if nums[mid] == nums[left] == nums[right]:
            left += 1
            right -= 1
            continue
        if nums[left] <= nums[mid]: #means left half is sorted
            if nums[left] <= target <= nums[mid]: #target is infact in left half
                right = mid - 1
            else:
                left = mid + 1
        else: #right half is sorted
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
    return False

print(foo([2,5,6,0,0,1,2], 0))