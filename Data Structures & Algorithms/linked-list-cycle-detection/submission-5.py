# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        # creating a set and see if visit before
        visited = set()

        if head == None:
            return False

        
        while head.next !=None:

            # check if in set before if so return False
            if head in visited:
                return True

            # add into set
            visited.add(head)

            # move head
            head = head.next
        
        return False
