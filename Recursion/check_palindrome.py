def foo(s):
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    return foo(s[1:-1])
#print(foo("racecar")) # True


def palindrome(string,idx,length):
    if idx >= length // 2:
        return True
    
    if string[idx] != string[length-idx-1]:
        return False
    
    return palindrome(string,idx+1,length)

print(palindrome('MADAM',0,len('MADAM'))) # True