def brute(arr):
    '''T.C = O(2n)
       S.C = O(x), x is the number of non zeros element, worst can be O(n)'''
    temp = []
    n = len(arr)

    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    for i in range(len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp), len(arr)):
        arr[i] = 0

    return arr



print(brute([1,0,20,3,0,4,0,5,0,0,8,0,4,0]))

def optimal(arr): #T. c = O(n)
    '''We'll be using two pointers approach.
    We'll keep j at the first index which is zero and will start i from j + 1
    i will kepp iterating and j will always point to a zero'''

    j = -1
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            j = i 
            break

    if j == -1:
        return arr #no zero exists
    
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j], arr[i]
            j += 1 #so that j starts pointing at zero element again
    
    return arr

print(optimal([1,0,20,3,0,4,0,5,0,0,8,0,4,0]))