def foo(arr,x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
        
    return -1

print(foo([1,2,3,4,5],4))