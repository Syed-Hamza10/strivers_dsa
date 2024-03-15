def foo(i):
    if i == 0:
        return 0 #base case
    return i + foo(i-1)

print(foo(6)) #21

#this is called functional recursion because the calculations happen in the function body and not in the function parameters.
