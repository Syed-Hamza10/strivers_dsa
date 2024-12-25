def foo(nums):
    '''an element is called a peak element if its strictly greater than its neighbors'''

    n = len(nums)

    if n == 1:
        return 0

    if nums[0] > nums[1]:
        #first element is the peak element
        return 0
    
    if nums[n-1] > nums[n-2]:
        return n-1 #last element is peak element
    
    low = 1, high = n - 2

    while low <= high:
        mid = low + (high - low) // 2

        if  nums[mid - 1] < nums[mid] > nums[mid + 1]: #no need to check if mid is 0 or n-1 since we dealt with that earlier
            return mid
        
        elif nums[mid] > nums[mid - 1]: #means peak element lies on the right 
            low = mid + 1
        
        elif nums[mid] > nums[mid + 1]: #means peak element lies on the left
            high = mid - 1
        else: #go to any direction, either left or right, you will find a peak element
            low = mid + 1