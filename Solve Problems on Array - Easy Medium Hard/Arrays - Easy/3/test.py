def sort_array(arr):

    n = len(arr)
    for i in range(n-1): # handles batches
        for j in range(n - 1): #handles passes
            if arr[j + 1] <= arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]    

    return arr


arr = [5,4,3,2,1]
print(sort_array(arr))