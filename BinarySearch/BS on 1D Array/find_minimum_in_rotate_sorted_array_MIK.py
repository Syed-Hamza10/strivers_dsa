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

def find_min_striver(nums):
    '''find the sorted part, update the min variable'''
    n = len(nums)
    left, right = 0 , n - 1
    mini = float('inf')

    while left <= right:
        mid = left + (right - left) // 2

        if nums[left] <= nums[mid]: # <= if it has only on element like [2,1]
            mini = min(nums[left], mini)
            left = mid + 1
        else:
            mini = min(nums[mid], mini)
            right = mid - 1

    return mini
print(find_min_striver([3,1,2]))