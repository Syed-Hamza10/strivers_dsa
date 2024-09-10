



def better(arr):
    hash = {}

    for i in arr:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for key, cnt in hash.items():
        if cnt == 1:
            return key    

print(better([1,1,2,3,3,4,4,5,5]))


def optimal_as_well(arr):

    return 2 * sum(set(arr)) - sum(arr)
print(optimal_as_well([1,1,2,3,3,4,4,5,5]))


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

#print(optimal([1,1,2,3,3,4,4,5,5]))