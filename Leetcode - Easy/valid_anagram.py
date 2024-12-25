from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    


def isAnagram_1(s, t):
    count = [0] * 26
    for i in s:
        count[ord(i) - ord('a')] += 1
    for i in t:
        count[ord(i) - ord('a')] -= 1

    for i in count:
        if i != 0:
            return False
    return True
