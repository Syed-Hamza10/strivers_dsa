def foo(arr, queries):
    n = len(arr)

    CumXOR = [0] * n
    CumXOR[0] = arr[0]

    for i in range(1, n):
        CumXOR[i] = CumXOR[i - 1] ^ arr[i] 
    
    res = []

    for query in queries:
        left = query[0]
        right = query[1]

        if left != 0:
            res.append(CumXOR[right] ^ CumXOR[left - 1])
        else:
            res.append(CumXOR[right])

    return res

print(foo([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))