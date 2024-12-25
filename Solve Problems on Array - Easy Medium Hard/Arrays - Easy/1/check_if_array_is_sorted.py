def foo(arr):
    for i in range(len(arr)-1):
        if arr[i + 1]>= arr[i]:
            pass
        else:
            return False
    return True
    
print(foo([1,2,3,4,5,6,5]))
        