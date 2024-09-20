def foo(n):
    return n -1
'''there will be n - 1 losers, every match has 1 winner and 1 loser, wo there will be n -1 losers'''

def alt(n):
    '''simulate what's given in the question'''

    result = 0
    while n > 1:
        if not n % 2:
            result += n // 2
            n //= 2
        else:
            result += (n - 1) // (2 + 1)
            n = (n - 1) // 2

    return result