#brute force
def brute_force(arr): #takes in NlogN
    sort = sorted(arr)
    return sort[-1]

def optimal(arr): # O(N)
    largest = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

print(optimal([1,2,7,4,5]))