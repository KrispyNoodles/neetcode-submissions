# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # create a set that collects all
        set_node = set()

        while headA:
            set_node.add(headA)
            headA = headA.next


        while headB:
            if headB in set_node:
                return headB
            headB = headB.next
        
        return None