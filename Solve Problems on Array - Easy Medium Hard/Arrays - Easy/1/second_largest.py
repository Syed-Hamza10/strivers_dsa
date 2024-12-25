def brute_force(arr): # NlogN + N
    arr = sorted(arr)
    largest = max(arr) # (N)
    slargest = 0
    n = len(arr)
    for i in range(n-2,0,-1):
        if arr[i] != largest:
            slargest = arr[i]
            return slargest
    

#print(brute_force([5,5,4,3,2,1]))

def better(arr): # O(2N) since there are two passes
    largest = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    
    slargest = -1 #provided you don't have any negative numbers

    for i in range(n):
        if arr[i] > slargest and arr[i] != largest:
            slargest = arr[i]
    return slargest

#print(better([5,5]))

def optimal(arr):
    largest = arr[0]
    slargest = -1
    for i in range(1,len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] > slargest and arr[i] < largest: #edge case
            slargest = arr[i]
    return (largest, slargest)

print(optimal([1,2,3,4,50,48,48,49]))
            