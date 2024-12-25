from typing import Optional

class Solution:
    def partition(self, head, x: int, ListNode):
        if not head or not head.next:
            return head

        small = smallHead = ListNode()
        large = largeHead =  ListNode()

        temp = head

        while temp:
            if temp.val < x:
                small.next = temp
                small = small.next
            else:
                large.next = temp 
                large = large.next
            
            temp = temp.next
        
        large.next = None
        small.next = largeHead.next

        return smallHead.next