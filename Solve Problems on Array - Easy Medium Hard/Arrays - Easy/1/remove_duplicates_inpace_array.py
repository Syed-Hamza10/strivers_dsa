#bring in all the unique numbers to the beginning, don't care about the rest
def brute_force(arr): # NlogN + N
    st = set()
    for i in arr:
        st.add(i)
    idx = 0
    for i in st:
        arr[idx] = i
        idx += 1
    return arr,

print(brute_force([1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,7,8]))


def optimal(arr): #using Two Pointer Approach, O(N), it will only work on sorted arrays
    
    i = 0

    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i + 1] = arr[j]
            i += 1
    return arr #number of unique elements
print(optimal([1,7,1,2,2,2,3,3,3,4,4,5,5,6,6,7,8]))

def list_comprehension(arr):
    res = []
    arr = [res.append(x) for x in arr if x not in res]
    return res
print(list_comprehension([1,2,3,4,5,5]))