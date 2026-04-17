# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # creating a head and a temp node
        # head is the start and temp is a pointer to keep
        head = ListNode()
        temp = head

        # ensure that both are there
        while list1 and list2:

            # add list1 and move it
            # adding the smaller value in
            if list2.val >= list1.val:
                temp.next = list1
                list1 = list1.next

            else:
                temp.next = list2
                list2 = list2.next


            # shift the temp after each, if not it will be only adding one node ever while loop only
            temp = temp.next

        # checking after eveyrthing and adding to the end
        if list1 is not None:
            temp.next = list1
        if list2 is not None:
            temp.next = list2

        return head.next

