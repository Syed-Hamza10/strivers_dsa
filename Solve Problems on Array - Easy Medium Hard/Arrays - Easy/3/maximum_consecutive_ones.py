def optimal(arr):

    max_ones = 0
    cnt = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
            # if cnt > max_ones:
            #     max_ones = cnt OR do the following

            max_ones = max(max_ones, cnt)
        else:
            cnt = 0

    return max_ones if max_ones > 0 else -1


print(optimal([1,2,1,1,1,4,5,1,1,1,0]))