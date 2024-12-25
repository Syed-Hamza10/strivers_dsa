def foo(arr,idx,n):
    if idx >= len(arr) // 2:
        return
    
    arr[idx] , arr[n- idx - 1] = arr[n - idx -1] , arr[idx]

    foo(arr,idx+1, n)

arr = [1,2,3,4,5,6,7,8]

n = len(arr)

foo(arr,0,n)

print(arr)