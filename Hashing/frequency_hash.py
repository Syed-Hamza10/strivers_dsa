def foo():
    n = int(input())
    arr = list(map(int, input().split()))
    hash = [0] * (100000) #precomputation
    for i in range(n):
        hash[arr[i]] += 1

    q = int(input())
    while q:
        x = int(input())
        print(hash[x])
        q -= 1

foo()


