# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# trying to solve now when there is multiple Listnodes
from typing import List

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

            # checking for empty lists
            if not lists:
                return None
            
            # merge one by one
            # merge one and two first
            # then the outcome merge with three
            first_node = lists[0]

            for index in range(1, len(lists)):
                
                first_node = self.mergeTwoLists(first_node, lists[index])
            
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