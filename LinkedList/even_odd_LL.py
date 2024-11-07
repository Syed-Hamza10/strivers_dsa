# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        
        if not head:
            return None

        odd = head
        even = evenStart = head.next

        if even is None:
            return odd

        while even and even.next:
            odd.next = even.next
            even.next = odd.next.next

            odd = odd.next
            even = even.next
        
        odd.next = evenStart
        return head
        