def removeDuplicates( nums) -> int:
        st = set()

        for i in nums:
            st.add(i)

        idx = 0
        for i in st:
            nums[idx] = i
            idx +=1

        n = len(st)
        return (n, nums)

def optimal(nums):
    n = len(nums)

    i = 0

    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i+1, nums 


#print(removeDuplicates([11,22,33,44,5555,66,66,77,77]))
#print(optimal([11,22,33,44,5555,66,66,77,77]))


def union(nums1, nums2):
     
    for i in nums2:
        if i not in nums1:
            nums1.append(i)
    nums1.sort()
    return nums1

print(union([1,2,3,4,5], [1,2,3,6,7]))