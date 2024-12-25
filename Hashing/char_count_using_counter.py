from collections import Counter
cnt = Counter()
def foo():
    string = 'my name is doraemon'
    for i in range(len(string)):
        cnt[string[i]] +=1
    q = int(input())
    while q:
        x = input()
        print(cnt[x])
        q -= 1
foo()
