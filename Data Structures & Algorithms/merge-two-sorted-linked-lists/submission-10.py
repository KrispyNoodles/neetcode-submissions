# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # to return the last element and handle cases where either list is none
        if list1 is None:
            return list2

        if list2 is None:
            return list1    

        # shift list2
        if list1.val >= list2.val:

            # adjust list2's next
            # feed in the node after list2 and current list1
            list2.next = self.mergeTwoLists(list1, list2.next)
            
            # return list2 back
            return list2
        
        else:

            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

        
