count = 0

def foo():
    global count
    print(count)
    count += 1
    if count == 998:
        return
    foo()

foo()