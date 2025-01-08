# def brute(arr):
#     i = j = 0 

#     n = len(arr)

#     while j < n:
#         while arr[j] != 0:
#             j += 1
#         arr[i], arr[j] = arr[i], arr[j
                                     
                                     
#                             ]
        

def optimal(arr):
    '''The algo is called Dutch National Flag Algo
    We have all zeros from 0 to low - 1 
    low to  mid - 1 all ones
    all twos from high + 1 and n -1
    else mid to high is everything unsorted'''
    n = len(arr)

    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low] , arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        
        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr



print(optimal([1,2,0,2,1]))
        