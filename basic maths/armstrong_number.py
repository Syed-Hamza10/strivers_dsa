def count_digit(n):
    count = 0
    while n>0:
        count += 1
        n = int(n/10)
    return count 


def foo(n):
    dup = n
    sum = 0
    count = count_digit(n)
    while n>0:
        last_digit = n%10
        sum += (last_digit**count)
        n = int(n / 10)
    return True if sum == dup else False
print(foo(1634))    

   