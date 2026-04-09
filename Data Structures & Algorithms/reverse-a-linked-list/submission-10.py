# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # creating a variable to save
        curr = head
        curr_new_head = None

        while curr != None:

            # save the next curr
            next_curr = curr.next

            # reassign
            curr.next = curr_new_head

            # preparing for the next loop
            curr_new_head = curr
            curr = next_curr

        return curr_new_head