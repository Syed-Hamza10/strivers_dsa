class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
def arr_to_ll(arr):
    head = Node(arr[0])
    i, n = 1, len(arr)
    temp = head

    while i < n:
        temp.next = Node(arr[i])
        temp = temp.next
        i += 1

    return head

def traverse_ll(head):
    temp = head
    while temp:
        print(temp.val, '->', end = " ")
        temp = temp.next
        
    print('Null')
head = arr_to_ll([1,2,3,4,5])
traverse_ll(head)
    
