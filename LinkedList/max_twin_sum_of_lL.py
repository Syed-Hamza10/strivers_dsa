def pairSum(head):
    if not head.next:
        return head.val

    res = []
    temp = head

    while temp:
        res.append(temp.val)
        temp = temp.next

    i, j = 0, len(res) - 1
    maxSum = 0
    
    while i < j:
        maxSum = max(res[i] + res[j], maxSum)
        i += 1
        j -= 1
    
    return maxSum