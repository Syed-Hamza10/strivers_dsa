import math
def calculateTotalHours(v, hourly):
    totalH = 0
    n = len(v)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH

def minimumRateToEatBananas(piles, h):
    low = 1
    high = max(piles)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        totalH = calculateTotalHours(piles, mid)
        if totalH <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low