def foo(num):
    low = 1
    high = num
    ans = 1
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid <= num:
            ans = mid
            low = mid + 1
        
        else: #mid * mid > num:
            high = mid - 1
        
    return high #or return ans
print(foo(17))