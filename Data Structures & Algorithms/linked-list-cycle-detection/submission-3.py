# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # creating a list to store all the nodes that you have visited
        # if the node is the same, congrats you are in a cycle

        # use a set instead of an array
        s = set()

        while head:

            if head in s:
                return True

            s.add(head)

            # move head
            head = head.next
        
        return False

# time complexity of O(n)
# space complexity of O(n)