# other reattempts
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create a dummy head
        head = ListNode(-1)
        tail = head

        # while both is not empty
        # as soon as one is empty then the while loop breaks
        while list1 and list2:
            
            # add list 2 into the tail
            if list1.val >= list2.val:

                tail.next = list2
                # same as tail = tail.next
                # tail = list2
                list2 = list2.next

            else:
   
                tail.next = list1

                # same as tail = tail.next
                # tail = list1 
                list1 = list1.next
            
            tail = tail.next
        
        # checking for leftovers
        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return head.next