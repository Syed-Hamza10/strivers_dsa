def foo(i):
    if i > 5:
        return
    foo(i+1)
    print(i) #this is where it backtracks to

foo(1)