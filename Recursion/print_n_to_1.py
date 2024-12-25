def foo(n):
    if n == 0:
        return
    
    print(n)
    foo(n-1)

foo(3)

def foo_alt(i,x):
    if i < 1:
        return
    print(i)
    foo_alt(i-1,x)
foo_alt(3,3)
