def fact(n,prod = 0):
    if n == 0:
        return prod
    return fact(n-1, prod * n)

print(fact(5,1))

#fact(2,3)
#fact(1,6)
#fact(0,6) returns 6