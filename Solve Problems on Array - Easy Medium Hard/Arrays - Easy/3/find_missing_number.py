def brute(arr,n):
    for i in range(len(arr)):
        if arr[i] == i + 1:
            pass
        else:
            return i + 1
    return -1

print(brute([1,2,4,5],5))

def better(arr,n): # T.C O(n x n) SC ( n )
    '''We'll create a hash of size n + 1
    then iterate over our list and incremeting the index in hash
    we find in our list
    In the end, return the INDEX which have 0 value'''
    hash = [0 for _ in range(n+1)]

    for i in range(len(arr)):
        hash[arr[i]] += 1 

    for i in range(1,n):
        if hash[i] == 0:
            return i
        
print(better([2,3,4,5],5))