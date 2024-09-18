def foo(string):
    maxChar = 0

    for i in range(2, len(string)):
        if string[i] == string[i - 1 ] and string[i - 1] == string[i - 2]:
            maxChar = max(maxChar, int(string[i]))

    return str(maxChar) * 3

print(foo("6777133339"))