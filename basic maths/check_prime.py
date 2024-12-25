def foo(n):
    x = 1
    count = 0
    while x<=n:
        if n%x == 0:
            count += 1
        x += 1    
    return True if count == 2 else False        

print(foo(37))