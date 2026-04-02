from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # creating a dummy node
        dummy_node = ListNode(-1)

        # initialise the head and tail to it?
        head_pointer = dummy_node
        tail_pointer = dummy_node

        while list1 != None and list2 != None:

            # include list2 node in
            if list1.val >= list2.val:

                # use the pointer of list 2
                tail_pointer.next = list2

                tail_pointer = list2

                # move list 2
                list2 = list2.next

            # include list 1 in and move it
            else:
                tail_pointer.next = list1

                tail_pointer = list1

                # moving list 1
                list1 = list1.next

        # checking if there is any left
        # this would mean that the node in there is the largest value, since it will clear the smaller ones first

        if list1 != None:
            tail_pointer.next = list1
        
        if list2 != None:
            tail_pointer.next = list2

        # return the head_pointer next as it will point to the first element
        return head_pointer.next