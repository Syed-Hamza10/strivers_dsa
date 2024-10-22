def bin2int(s):
    if not s:
        return 0
        
    result = 0
    i = 1
    n = len(s)
    
    for char in s:
        result += (int(char) * (2 ** (n - i))) 
        i += 1
    return result

print(bin2int('101'))