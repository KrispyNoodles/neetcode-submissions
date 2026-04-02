# trying to solve now when there is multiple Listnodes
from typing import List

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # merge one by one
        # merge one and two first
        # then the outcome merge with three
        first_node = None

        for nodes in lists:

            if not first_node:
                first_node = nodes
                continue

            first_node = self.mergeTwoLists(first_node, nodes)

        return first_node
    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode(-1)
        tail = dummy_node

        # as long as list1 and list2 are not empty
        while list1 and list2:  

            # checking if which value is bigger
            if list1.val >= list2.val:

                # list2 becomes the new tail
                tail.next = list2

                # shift list2
                list2 = list2.next
            
            else:
                tail.next = list1
                list1 = list1.next

            # change the new tail
            tail = tail.next
    
        # checking if either is left
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy_node.next