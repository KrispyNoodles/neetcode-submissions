# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # base case
        if not head:
            return False
        
        # floyd cycle finding
        fast = head
        slow = head

        while fast.next and fast.next.next:

            
            # moving both
            # fast moves twice and slow moves once
            fast= fast.next.next
            slow = slow.next
        
            # if they meet means have loops
            if fast == slow:
                return True

        # if exit already means no loop
        return False