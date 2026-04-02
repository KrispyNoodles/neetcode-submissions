# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        curr_prev = None

        while curr != None:

            curr_next = curr.next

            # reassign the curr
            curr.next = curr_prev

            curr_prev = curr 

            curr = curr_next

        return curr_prev
        