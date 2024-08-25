def optimal(arr):
    '''
    5 xor 5 = 0
    0 xor 5 = 5 - The Number Itself !
    1 ^ 1 ^ 2 ^ 3 ^ 3 ^ 4 ^ 4 ^ 5 ^ 5
    0 ^ 2 ^ 0 ^ 0 ^ 0
    2
    The result of `1 XOR 1` is `0`.

In binary logic, XOR (exclusive OR) produces a `1` only if the two input bits are different. 
If both inputs are the same (either `0 XOR 0` or `1 XOR 1`), the result is `0`.
    '''

    xor = 0
    for num in arr:
        xor = xor ^ num
    return xor

print(optimal([1,1,2,3,3,4,4,5,5]))