 #Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
        
    def mergeTwoLists(self, list1, list2):

        ans = ListNode()
        dummyHead = ans

        while list1 and list2:
            if list1.val <= list2.val:
                ans.next = list1
                list1 = list1.next
                ans = ans.next
            else:
                ans.next = list2
                list2 = list2.next 
                ans = ans.next

        while list1:
            ans.next = list1
            ans = ans.next
            list1 = list1.next
        while list2:     
            ans.next = list2
            ans = ans.next
            list2 = list2.next
        return dummyHead.next