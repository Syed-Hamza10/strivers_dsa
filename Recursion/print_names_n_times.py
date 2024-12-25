def foo(n):
    if n == 0:
        return
    print('Hamza')
    foo(n-1)

#foo(5)

def foo1(i,n):
    if i > n:
        return #base case
    print('Hamza')
    foo1(i+1,n)
foo1(1,5)    

# T.C = O(N)
# S.C = O(N) we usualyy takes stack space