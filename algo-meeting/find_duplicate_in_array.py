def foo(nums):
    n = len(nums)

    slow = 0
    fast = 0

    while slow < n - 1:
        slow += 1
        slow = slow % n
        fast += 2
        fast = fast % n
        if nums[slow] == nums[fast]:
            return nums[slow]
print(foo([3,1,3,4,2]))