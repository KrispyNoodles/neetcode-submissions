# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # creating a dummy Node
        head = ListNode()

        # initialisation of the dummy
        dummy = head

        # while list 1 and list 2 are not None
        while list1 and list2:

            # add list 1 val
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next

            # add list 2
            else:
                dummy.next = list2
                list2 = list2.next
            
            # moving the dummy node
            dummy = dummy.next

        # checking if there are any left
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2

        # return the starting value
        return head.next
        