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


def optimal(arr): #using Two Pointer Approach, O(N)
    
    i = 0

    for j in range(len(arr)):
        if arr[i] != arr[j]:
            arr[i + 1] = arr[j]
            i += 1
    return arr #number of unique elements
print(optimal([1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,7,8]))