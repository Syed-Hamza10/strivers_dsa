def brute_force(arr): # NlogN + N
    arr = sorted(arr)
    smallest = min(arr)
    ssmallest = 0 
    n = len(arr)
    for i in range(0,n):
        if arr[i] != smallest:
            ssmallest = arr[i]
            return ssmallest
    

print(brute_force([5,5,4,3,2,1]))

def better(arr): # O(2N) since there are two passes
    smallest = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] < smallest:
            smallest = arr[i]
    
    ssmallest = 100000 
    

    for i in range(n):
        if arr[i] < ssmallest and arr[i] != smallest:
            ssmallest = arr[i]
    return ssmallest

print(better([5,5,4,3,2,1]))

def optimal(arr): # O(N)
    smallest = arr[0]
    ssmallest = float('inf')
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            ssmallest = smallest
            smallest = arr[i]
        elif arr[i] < ssmallest and arr[i] > smallest: #edge case
            ssmallest = arr[i]
    return (smallest, ssmallest)

print(optimal([10,20,3,50,2,1]))
            