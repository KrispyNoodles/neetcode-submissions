# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # creating a head and tail pointer
        # since the tail is initialise to the dummy, and all nodes are added after the tail/dummy,
        # we can trace all the values in there
        dummy = ListNode(-1)
        tail = dummy

        # while both list have values in them
        # check for the if condition to see which is smaller
        while list1 != None and list2 != None:
            
            # if list 2 value is smaller, then add list 2 value
            # keep adding the value
            # if it is bigger than this value but smaller than the next 
            if list1.val >= list2.val: 

                print(f"adding value {list2.val} from list2 to {tail.val}")
                # shift the tail
                tail.next = list2
                tail = list2

                # shift list2
                list2 = list2.next

            # else add list 1 value
            else:

                print(f"adding value {list1.val} from list1 to {tail.val}")
                tail.next = list1
                tail = list1

                list1 = list1.next
            
        # if list1 still has values, connect the tail's next to it
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2

        # return the head which is the beginning of this list
        return dummy.next
