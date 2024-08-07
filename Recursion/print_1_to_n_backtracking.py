def foo(i):
    if i < 1:
        return
    foo(i-1)
    print(i) #this is where it backtracks to

foo(4)

'''
f(4) waits in the stack
f(3) as well
f(2) also
f(1) also
f(0) returns then 
f(1) gets executed
f(2)
'''

