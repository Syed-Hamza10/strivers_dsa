def foo(n):
    x = 1
    while x<=n:
        if n%x == 0:
            print(x)
            x+=1
            continue
        x+=1
foo(36)     

#alternate (maybe) efficient method

def square_root(n):
    x = 0
    while x<n/2:
        if x*x == n:
            return x
        x += 1

def foo1(n):
    x = 1
    while x <= square_root(n):
        if n%x == 0:
            print(x)
            if x!= int(n/x):
                print(int(n/x))
                x+=1
                continue
            x+=1
            continue
        x+=1

foo1(36)
