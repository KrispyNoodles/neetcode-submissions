# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # saving the current nodea
        curr = head

        # waiting to be used
        temp = None

        while curr is not None:

            new_curr = curr.next

            curr.next = temp

            temp = curr

            curr = new_curr

        
        return temp 