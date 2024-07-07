#given an array, find highest and lowest character of array
def find_idx(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
def foo():
    arr = list(map(int, input().split()))
    #precompute
    hash = [0] * (max(arr) + 1)
    for i in arr:
        hash[i] += 1
    
#finding lowest frequency but greater than 0
    _max, _min = find_idx(hash,max(hash)), find_idx(hash,min([freq for freq in hash if freq > 0]))
    return _max, _min

print(foo())