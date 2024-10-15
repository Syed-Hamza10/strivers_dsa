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