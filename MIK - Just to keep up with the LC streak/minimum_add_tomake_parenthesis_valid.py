def foo(s):
    '''it is generally done with stack but we can do without stack as well'''

    size = 0
    open = 0

    for char in s:
        if char == '(':
            size += 1 #mtlb stack me push krna tha
        elif char == ')' and size > 0:
            size -= 1
        else:
            open += 1
    return open + size

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        for i in s:
            if len(stack) != 0 and i== ')' and stack[-1] == '(':
                stack.pop()

            else:
                stack.append(i)
   
        return len(stack)