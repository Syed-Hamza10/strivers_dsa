def foo(word, ch):

    j = 0
    count = 0
    for char in word:
        if char == ch:
            j = count
            break
        count +=1
    if j == 0 and word[0] != ch:
        return word
    
    i = 0
    word = list(word)
    while i <=j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1
    return ''.join(word)

def reversePrefix(self, word: str, ch: str) -> str:
        pos = word.find(ch) + 1
        a = word[:pos]
        b = word[pos:]

        return a[::-1] + b

print(foo("abcdefd", 'd'))