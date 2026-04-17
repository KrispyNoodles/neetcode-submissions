# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        new_next = None

        while curr != None:

            # saving the curr
            temp = curr

            # shifting
            curr = curr.next 

            # reassigning
            temp.next = new_next

            new_next = temp

        return new_next
