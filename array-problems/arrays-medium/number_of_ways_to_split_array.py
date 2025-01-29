from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        left_sum = res = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum

            if left_sum >= right_sum:
                res += 1

        
        return res