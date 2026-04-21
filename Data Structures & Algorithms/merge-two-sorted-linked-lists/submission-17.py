# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # creating a temp node
        head = ListNode(0)
        temp = head
        
        while list1 and list2:

            if list1.val >= list2.val:
                temp.next = list2
                list2 = list2.next

            else:
                temp.next = list1
                list1 = list1.next
            
            # moving the temp, if not it will just keep reassigning temp and not move anywhere
            temp = temp.next
        
        # checking if either is not empty to add to the end
        if list1:
            temp.next = list1
        
        if list2:
            temp.next = list2

        return head.next
