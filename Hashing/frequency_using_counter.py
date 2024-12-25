from collections import Counter
cnt = Counter()
def foo():
    arr = [1,1,2,3,4,5,2,1,2]
    for i in range(len(arr)):
        cnt[arr[i]] +=1
    q = int(input())
    while q:
        x = int(input())
        print(cnt[x])
        q -= 1
foo()
