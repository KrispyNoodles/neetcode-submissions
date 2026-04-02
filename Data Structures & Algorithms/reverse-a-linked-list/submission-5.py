# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # checking for empty
        if not head:
            return None

        
        final_new_head = head

        if head.next != None:

            # find the next final_new_head
            final_new_head = self.reverseList(head.next)

            # assign the head the head beside to point back to itsel
            head.next.next = head

        # ensure that the current head points to nothin
        head.next = None

        return final_new_head