def union(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)

    i = j = 0

    union = []

    while i < n1 and j < n2:
        if nums1[i] <= nums2[j]: #we're going to insert nums1[i]
            if len(union) == 0 or union[-1] != nums1[i]:
                pass


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(nums,start, end):
        

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    n = len(nums)

    
        
    reverse(nums[:k - 1])
    reverse(nums[k : n - 1])
    reverse(nums)
    print(nums)

rotate([1,2,3,4,5,6,7],3)