# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

def foo(words, chars):
    frequency = [0] * 26
    for char in chars:
        frequency[ord(char) - ord('a')] += 1 #to access that specific character, a - a = 0, b - a = 1, 1 per b para

    result = 0

    for word in words:
        WordCount = [0] *  26
        for ch in word:
            WordCount[ord(ch) - ord('a')] += 1

        possible = True
        for i in range(26):
            if WordCount[i] > frequency[i]:    
                possible = False
                break

        if possible:
            result += len(word)
    return result

print(foo(["cat","bt","hat","tree"], chars = "atach"))


def countCharacters(words, chars: str):
    d = dict(int)
    for char in chars: d[char] += 1

    res = 0
    for word in words:
        can_form = True
        for char in word:
            if word.count(char) > d[char]:
                can_form = False
                break
        if can_form:
            res += len(word)
    return res