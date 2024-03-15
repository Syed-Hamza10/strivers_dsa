#we have to get a sum of first n numbers

def foo(i, sum = 0):
    if i == 0:
        return sum
    return foo(i-1, sum+i)

print(foo(6)) #21

#we define a function foo that takes two arguments i and sum. The base case is when i is 0, we return the sum. Otherwise, we call foo with i-1 and sum+i.
#calculations happen in fuction parameters and not in the function body. This is called parametrized recursion.