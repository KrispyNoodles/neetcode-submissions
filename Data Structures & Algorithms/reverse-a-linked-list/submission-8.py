# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # node being work wiht
        curr_node = head
        
        # node that will be use to assign to current
        prev_node = None

        while curr_node != None:

            # saving the next node to work with
            next_node = curr_node.next

            # reassign the node's next
            curr_node.next = prev_node

            # using the current node before it is being reassinged
            prev_node = curr_node

            # moive the current_node to be the next
            curr_node = next_node

        return prev_node        