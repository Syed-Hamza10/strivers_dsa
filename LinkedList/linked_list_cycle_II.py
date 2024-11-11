# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        
        slow = fast = temp = head
        idx = 0

        if not head or not head.next:
            return None

        while fast and fast.next:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        if slow!= fast:
            return None

        while True:
            if slow == temp:
                return slow
            temp = temp.next
            slow = slow.next
             #or temp 


class Solution:
    def detectCycle(self, head):
        fast, slow = head, head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                slow = head
                while(slow is not fast):
                    fast = fast.next
                    slow = slow.next
                return slow
        return None