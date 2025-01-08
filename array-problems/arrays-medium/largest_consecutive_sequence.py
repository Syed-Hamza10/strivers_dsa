my_list = [0] * 50

global_variabe = 42

def brute(nums):
    nums = sorted(nums)
    n = len(nums)
    count = 1

    for i in range(n-1):
        if nums[i + 1] == nums[i] + 1:
            count += 1

    return count




def optimal(nums):
    st = set(nums)
    longest = 1
    if len(nums) == 0:
        return 1

    '''First, we will convert it to set to avoid duplicates.
    uske baad, ham check kre ge agar (element - 1) set me exists krta to ham counting use start nahi kre ge kiyunke
    sequence me bheech me se start krne ka faida nahi.
    agar element - 1 set me nahi hai to counting start kre ge, or jab tak element + 1 set me hai
    tab tak counting krte chale jaye ge. end per longest me max ko rakhwa do'''

    for num in st:
        if (num - 1) not in st:
            count = 1
            x = num
            while (x + 1) in st:
                x += 1
                count += 1
            longest = max(longest, count)

    return longest

print(optimal([100,4,200,1,3,2]))


