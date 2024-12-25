def optimal(arr): # O(n), no extra space used
    n = len(arr)
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]

    arr[n-1] = temp
    return arr

print(optimal([1,2,3,4,5,6,7,8,9]))

''' since we just have to move it by one place, you can simply keep the first element in temp
variabe, then loop over the entire list, shift every element before, and after loop, put temp 
in the last'''