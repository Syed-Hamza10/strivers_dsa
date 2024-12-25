def foo(strs):
    
    n = len(strs)
    str_len = len(strs[0])

    cnt = 0

    for col in range(str_len):
        for row in range(n-1):

            if strs[row][col] > strs[row + 1][col]:

                cnt += 1
                break


    return cnt

print(foo(["zyx","wvu","tsr"]))
