# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        new_next = None

        # the new head will from 0 to 1 to 0 to none

        while curr != None:

            print(curr.val)

            # retrieve the old next
            old_next = curr.next
            
            # update the new next
            curr.next = new_next

            # save the new next to be the curr
            new_next = curr

            # move the pointer
            curr = old_next

        # never return anything?
        return new_next

# time complexity to be O(n) because loop through all the different elements
# space compleity of O(1)