def striver(nums, target):
    n = len(nums)

    def lower_bound(nums, target):
        n = len(nums)
        left, right = 0, n - 1
        ans = n

        while left <= right:
            mid = left + (right- left) // 2

            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def upper_bound(nums, target):
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right- left) // 2

            if nums[mid] > target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
    lb = lower_bound(nums, target)
    hb = upper_bound(nums, target)

    if lb == n or nums[lb] != target:
        return [-1,-1]
    
    return [lb, hb -1]
class Solution:

    def findLeft(self, nums, n, target):
        l = 0
        r = n - 1

        left_most = -1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                left_most = mid
                r = mid - 1
            elif nums[mid] >target:
                r = mid - 1
            else:
                l = mid + 1

        return left_most

    def findRight(self, nums, n, target):
        l = 0
        r = n - 1

        right_most = -1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                right_most = mid
                l = mid + 1
            elif nums[mid] >target:
                r = mid - 1
            else:
                l = mid + 1 
        return right_most   

    def searchRange(self, nums, target):
        left_most = -1
        right_most = -1

        n = len(nums)

        left_most = self.findLeft(nums, n, target)
        right_most = self.findRight(nums,n , target)

        return [left_most, right_most]
    
print(striver([1,2,3,4,4,5,6,7,8,9], 4))