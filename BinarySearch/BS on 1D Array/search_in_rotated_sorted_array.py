def foo(nums, target):
    n = len(nums)

    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        
        if nums[mid] == target:
            return True
        
        #check if left is sorted

        if nums[left] <= nums[mid]:
            if nums[left] <= target and target <= nums[mid]: #check if it lies on left
                right = mid - 1
            else:
                left = mid + 1
        else: #right sorted - one half will always be sorted
            if nums[mid] <= target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1     
print(foo([4,5,6,7,0,1,2], 0))