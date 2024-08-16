def brute(arr, d): # T:C O (n + d), S.C = O(d)
    '''d is the number of places to rotate'''
    
    n = len(arr)
    d = d % n #because when we move n times it becomes the same array

    #making temp array to store the elements to shift

    temp = arr[:d] # O(d)

    
    #shifting

    for i in range(d,n): #O(n-d)
        arr[i - d] = arr[i]

    #putting back temp

    j = 0
    for i in range(n-d,n): # O( d )
        #instead of using j, you can also use temp[i-(n-d)]
        arr[i] = temp[j]
        j += 1

    return arr

#print(brute([1,2,3,4,5,6,7],6))


def optimal(arr,d): # T.C O(2n), S.C - O(1), we're not using any EXTRA space
    '''The intuition is to reverse from 0th index to d, then from d to n, then reverse the entire array
    [1,2,3,4,5,6,7] lets say we have to shift it by 3

    1st time : [3,2,1,4,5,6,7]
    2nd time : [3,2,1,7,6,5,4]
    3rd time : [4,5,6,7,1,2,3]'''


    def reverse(arr, start, end):
        while start < end :
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
    n = len(arr)

    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0 , n - 1)

    return arr

print(optimal([1,2,3,4,5,6,7],3))