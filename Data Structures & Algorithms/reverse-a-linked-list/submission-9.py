# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # saving this current node
        current_node = head

        # new next node
        new_next_node = None

        while current_node != None:

            # save the next node here
            # saving the next node
            old_next_node = current_node.next

            # re-assign
            current_node.next = new_next_node

            new_next_node = current_node

            # reassign the current node
            current_node = old_next_node

        return new_next_node

