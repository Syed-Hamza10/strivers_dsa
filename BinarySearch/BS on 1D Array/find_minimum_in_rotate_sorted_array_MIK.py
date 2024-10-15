def find_min(nums):
    n = len(nums)

    start, end = 0, n-1
    
    if len(nums) == 1:
        return nums[0]

    while start < end: #sirf less than kre ge warna loop me phans jaye ge, kiyunke end ko mid kr rahe not mid-1
        mid = start + (end-start)//2

        if nums[mid] > nums[end]:
            start = mid + 1 # mid + 1 isi liye kiyunke mid to ho hi nahi skta, hai na?
        else: #mtlb mid chota hai end wale se
            end = mid #mid itself bhi min hoskta, smjha?
    return nums[end] #At the end of the loop, start and end are equal and point to the minimum value.

print(find_min([2,1]))


