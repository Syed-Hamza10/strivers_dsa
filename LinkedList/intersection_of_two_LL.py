<<<<<<< HEAD
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        lenA = 0
        lenB = 0
        tempA = headA 
        tempB = headB
        while tempA:
            lenA += 1
            tempA = tempA.next

        while tempB:
            lenB += 1
            tempB = tempB.next

        diff = abs(lenA - lenB)
        tempA = headA 
        tempB = headB


        if lenA > lenB:
            while diff and tempA:
                tempA = tempA.next
                diff -= 1
        else:
            while diff and tempB:
                tempB = tempB.next
                diff -= 1
        while tempA and tempB:
            if tempA == tempB:
                return tempA
            tempA, tempB = tempA.next, tempB.next

=======
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        lenA = 0
        lenB = 0
        tempA = headA 
        tempB = headB
        while tempA:
            lenA += 1
            tempA = tempA.next

        while tempB:
            lenB += 1
            tempB = tempB.next

        diff = abs(lenA - lenB)
        tempA = headA 
        tempB = headB


        if lenA > lenB:
            while diff and tempA:
                tempA = tempA.next
                diff -= 1
        else:
            while diff and tempB:
                tempB = tempB.next
                diff -= 1
        while tempA and tempB:
            if tempA == tempB:
                return tempA
            tempA, tempB = tempA.next, tempB.next

>>>>>>> 1aad2de (Reorder linked-list)
        return None