def foo(num):
    def check_odd_str(num):
        if int(num) % 2:
            return True
        return False

    n = len(num)

    for i in range(n-1, -1, -1):
        if check_odd_str(num[i]):
            return num[0:i+1]
    return "" 

print(foo("35427"))       