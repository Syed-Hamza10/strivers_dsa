def possible(array, day,m, k):
    '''You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and
 then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
 If it is impossible to make m bouquets return -1.
    '''

    cnt = 0
    number_of_B = 0

    n = len(array)

    for i in range(n):
        if array[i] <= day:
            cnt += 1
        else:
            number_of_B += (cnt // k)
            cnt = 0
    number_of_B += (cnt // k)

    return number_of_B >= m

def brute(bloomDay, m,  k ):
    val = m*k
    n = len(bloomDay)
    if val > n:
        return -1
    mini = min(bloomDay)
    maxi = max(bloomDay)

    for i in range(mini, maxi + 1):
        if possible(bloomDay, i, m, k):
            return i
    return -1