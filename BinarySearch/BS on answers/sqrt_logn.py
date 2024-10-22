def foo(num):
    low = 1
    high = num
    ans = 0
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid == num:
            ans = mid
            return ans
        
        elif mid * mid > num:
            high = mid - 1
        else:
            low = mid + 1
    return high
print(foo(17))