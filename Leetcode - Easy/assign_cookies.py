def findContentChildren(g, s):
        g.sort()
        s.sort()

        child_index = cookie_index = 0

        m = len(g)
        n = len(s)

        count = 0

        while child_index < m and cookie_index < n:
            if s[cookie_index] >= g[child_index]:
                
                child_index += 1
                cookie_index += 1
            else:
                cookie_index += 1
        return child_index

print(findContentChildren([1,2,3], [1,1]))