def foo(arr):

    n = len(arr) - 1

    for i in range(n, -1, -1):

        if arr[i] == 0:

            for j in range(n, i,  -1):
                arr[j ] = arr[j - 1]

class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        size = len(arr)
        while i < size:
            if arr[i] == 0 and i+1 < len(arr):
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i += 1
                

        