#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next:
            return head
        tail = head
        length = 1

        while tail.next:
            tail = tail.next
            length += 1

        if k % length == 0:
            return head #no need to rotate

        k = k % length

        temp = head
        for i in range(length - k - 1):
            temp = temp.next

        new_head = temp.next
        temp.next = None

        tail.next = head

        return new_head
        