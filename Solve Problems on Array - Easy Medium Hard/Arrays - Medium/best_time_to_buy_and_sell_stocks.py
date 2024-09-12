def optimal(arr):
    mini, profit = arr[0], 0
    n = len(arr)

    for i in range(1, n):
        cost = arr[i] - mini

        profit = max(cost, profit)

        mini = min(arr[i], mini)

    return profit

print(optimal([7,6,4,3,1]))