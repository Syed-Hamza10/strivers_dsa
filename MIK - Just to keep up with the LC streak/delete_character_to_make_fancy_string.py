def makeFancyString(s: str) -> str:

    ans = ''
    freq = 0

    if len(s) < 3:
        return s
    
    ans += s[0]
    freq = 1

    for i in range(1, len(s)):
        
        if ans[-1] == s[i]:
            freq += 1
            if freq < 3 :
                ans += s[i]
        else:
            freq = 1
            ans += s[i]

    return ans

print(makeFancyString("leeetcode"))