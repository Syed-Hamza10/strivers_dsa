def foo():
    n = int(input())
    string = input()
    #pre computation
    hash = [0] * 256
    for i in range(n):
        hash[ord(string[i])] += 1
    q = int(input())

    while q:
        x = input()
        ascii = ord(x)
        #fetch
        print(hash[ascii])
        q -= 1

foo()