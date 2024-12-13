#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):

        t1, t2 = l1, l2
        carry = 0
        dummy = ListNode(-1)
        curr = dummy

        while t1 or t2:
            my_sum = carry
            carry = 0
            if t1: 
                my_sum += t1.val
                t1 = t1.next
            if t2:
                my_sum += t2.val
                t2 = t2.next

            if my_sum >= 10:
                carry = my_sum // 10
            my_sum %= 10

            curr.next = ListNode(my_sum)
            curr = curr.next     
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next