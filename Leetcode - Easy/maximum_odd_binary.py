def foo(s):
    s = list(s)
    n = len(s)
    res = ['0'] * len(s)
    
    idx = 0
    for i in s:
        if i == '1' and res[n - 1] == '0':
            res[n - 1] = '1'
            continue
        elif i == '1':
            res[idx] = '1'
            idx += 1
    return ''.join(res)

def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = s.count('0')
        result = "1" * (ones-1) + "0" * zeros + "1"
        return result

print(foo('01010'))