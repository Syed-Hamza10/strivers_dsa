
def halvesAreAlike(s: str) -> bool:
    vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", 'O', "U"]

    n = len(s)

    first_half = s[ : n//2]
    second_half = s[n//2 : ]

    count_first = count_second = 0
    for s in first_half:
        if s in vowels:
            count_first+=1

    for s in second_half:
        if s in vowels:
            count_second += 1

    return count_second == count_first

print(halvesAreAlike('textbook'))