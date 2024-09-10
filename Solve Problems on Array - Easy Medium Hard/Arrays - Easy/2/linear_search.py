def foo(arr,x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
        
    return -1

print(foo([1,2,3,4,5],4))




'''
[5,4,3,2,1]
1st pass
[4,5,3,2,1]
4,3,5,2,1
4,3,2,5,1
4,3,2,1,5

2nd pass

'''