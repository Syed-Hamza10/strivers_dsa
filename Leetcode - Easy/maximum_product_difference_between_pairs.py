def foo(nums):

    maxi = -float('inf')
    sec_maxi = -float('inf')

    for i in nums:
        if i >= maxi:
            sec_maxi = maxi
            maxi = i
        elif i < maxi and i > sec_maxi:
            sec_maxi = i

    mini = float('inf')
    sec_mini = float('inf')

    for i in nums:
        if i <= mini:
            sec_mini = mini
            mini = i
        elif i > mini and i < sec_mini:
            sec_mini = i
    
    res = (maxi * sec_maxi) - (mini * sec_mini)
    return res if res > 0 else 0

print(foo([10,10,10,10]))