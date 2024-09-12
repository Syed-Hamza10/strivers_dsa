def foo(arr):
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]

    res = []

    for i, j in zip(pos, neg):
        res.append(i)
        res.append(j)

    return res


def optimal(arr):
    pos = 0
    neg = 1

    res = [0] * len(arr)

    i = 0

    while i < len(arr):
        if arr[i] > 0:
            res[pos] = arr[i]
            pos += 2
        elif arr[i] < 0:
            res[neg] = arr[i]
            neg += 2
        i += 1    
    
    print(res)
optimal([3,1,-2,-5,2,-4])
