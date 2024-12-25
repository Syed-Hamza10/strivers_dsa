def foo(arr,first,last):
    if first >= last:
        return
    
    arr[first], arr[last] = arr[last], arr[first]
    foo(arr, first+1, last-1)

arr = [1,2,3,4,5,6,7,8]
foo(arr,0,len(arr) - 1)

print(arr)