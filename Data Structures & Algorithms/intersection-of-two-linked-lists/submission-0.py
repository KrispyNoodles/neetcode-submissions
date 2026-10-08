# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        

        # run all values of head A to all values of headB

        referA = headA
        
        while referA:

            # reset the node to be the beginning
            referB = headB

            while referB:

                if referA == referB:
                    return referA

                referB = referB.next

            # check
            referA = referA.next
        
        # else return 
        return None