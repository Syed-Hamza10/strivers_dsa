def foo(n):
    if n <= 1:
        return n
    
    last = foo(n-1)
    second_last = foo(n-2)
    return last + second_last

print(foo(4))