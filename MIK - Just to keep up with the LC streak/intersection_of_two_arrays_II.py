def foo(nums1, nums2):
    '''using a map'''

    freq_nums1 = {}
    res = []

    for ele in nums1:
        if ele in freq_nums1:
            freq_nums1[ele] += 1
        else:
            freq_nums1[ele] = 1

    for ele in nums2:
        if ele in freq_nums1 and freq_nums1[ele] != 0:      
            res.append(ele)
            freq_nums1[ele] -= 1
    return res

print(foo([4,9,5],[9,4,9,8,4]))

def foo2(nums1, nums2):
    '''by sorting both arrays'''

    nums1.sort()
    nums2.sort()

    i = j = 0

    res = []
    n1, n2 = len(nums1), len(nums2)

    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i+= 1
        else:
            j += 1
    return res

print(foo2([4,9,5],[9,4,9,8,4]))