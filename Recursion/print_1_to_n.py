def foo(i,n):
    if i > n:
        return #base case
    
    print(i)
    foo(i+1,n)

foo(1,5)
