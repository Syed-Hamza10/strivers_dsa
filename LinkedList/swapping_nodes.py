# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k: int):
    
        temp = head
        k1 = k
        while k1 > 1:
            temp = temp.next
            k1 -= 1

        node_1 = temp
        temp = head

        #length of list
        length = 0

        while temp:
            length += 1
            temp = temp.next

        cnt = 0
        temp = head
        k2 = length - k + 1
        while cnt < (length - k):
            temp = temp.next
            cnt += 1
        
        node_2 = temp

        node_1.val, node_2.val = node_2.val, node_1.val

        return head
    
    
    def swapNodes(self, head, k: int):


        temp = head
        
        for _ in range( k - 1):
            temp = temp.next

        person1 = temp
        person2 = head
        while temp.next:
            person2 = person2.next
            temp=temp.next

        person1.val, person2.val = person2.val, person1.val

        return head