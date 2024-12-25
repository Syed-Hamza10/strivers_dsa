class Solution:
    def singleNonDuplicate(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        n = len(nums)

        if n == 1:
            return nums[0]
        while left <= right:
            mid = left + (right - left)//2

            if (n - 1 - mid) % 2 == 0: #mtlb right side per even numbers are left
                if mid != n -1 and nums[mid + 1] == nums[mid]:
                    left = mid + 1 #go left
                else:
                    if nums[mid] != nums[mid - 1]:
                        return nums[mid]
                    right = mid - 1 #go right
            else: #odd
                if nums[mid + 1] == nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return nums[mid] 
                    