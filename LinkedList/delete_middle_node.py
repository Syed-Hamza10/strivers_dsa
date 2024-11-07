# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def deleteMiddle2(self, head):
        
        if not head or not head.next:
            return None

        length = 0

        temp = head

        while temp:
            length += 1
            temp = temp.next

        target = length // 2
    

        curr = head
        cnt = 0

        while cnt < target - 1:
            cnt += 1
            curr = curr.next



        curr.next = curr.next.next
   
        return head

    def deleteMiddle(self, head):
        
        if head.next is None:
            return None

        slow, fast = head, head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next    
        
        return head

    def deleteMiddle3(self, head):

        if not head or not head.next:
            return None

        slow = fast = head

        prev = None

        while fast and fast.next:
            prev = slow

            slow = slow.next 
            fast = fast.next.next 

        prev.next = slow.next 

        return head