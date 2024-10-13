def foo(flowerbed, n):
    x = len(flowerbed)
    count = 0

    if n == 0:
        return True
    for i in range(x):
        if flowerbed[i] == 0:
            left_empty = (i == 0 or flowerbed[i-1] == 0)
            right_empty = (i == x - 1 or flowerbed[i + 1] == 0)
            if left_empty and right_empty:
                n -= 1
                flowerbed[i] = 1
    return True if n == 0 else False

print(foo([1,0,0,0,1], 1))