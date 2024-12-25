def brute(weights, days):
    res = 0
    n = len(weights)
    min_cap = max(weights)
    for i in range(n):
        cap = weights[i]
        for j in range(i + 1, n):
            if cap + weights[j] < min_cap:
                cap += weights[j]
            else:
                break
    return min_cap

print(brute([1,2,3,4,5,6,7,8,9,10], 5))


class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        
        def canShip(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days 

        l, r = max(weights), sum(weights)
        res = r 
        while l <= r:
            cap = l + (r - l) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res
        