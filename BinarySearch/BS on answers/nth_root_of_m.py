def brute(n , m):

    for i in range(1, m):
        if i ** n == m:
            return i
        elif i ** n > m:
            return -1

#print(brute(3, 27))

def optimal(n, m):

    low = 1
    high = m

    ans = 1

    while low <= high:
        mid = low + (high - low) // 2
        
        if mid ** n == m:
            return mid
        elif mid ** n > m:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(optimal(6, 4096))