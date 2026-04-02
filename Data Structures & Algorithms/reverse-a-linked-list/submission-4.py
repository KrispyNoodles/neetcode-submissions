# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev_curr = None

        while curr != None:

            # retrieve the next value
            next_curr = curr.next

            # reassign
            curr.next = prev_curr

            # save the curr to be the next prev_curr
            prev_curr = curr 

            # and move to the next curr
            curr = next_curr

        return prev_curr
        