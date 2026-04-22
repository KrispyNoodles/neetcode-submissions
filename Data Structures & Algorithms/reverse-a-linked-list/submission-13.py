# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        # temp will be used to store the new next
        temp = None

        while curr:

            new_curr = curr.next
            curr.next = temp

            temp = curr
            curr = new_curr

        return temp