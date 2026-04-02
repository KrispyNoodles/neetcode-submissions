# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # creating a head and tail pointer
        head = ListNode(-1)
        tail = head

        # while both list have values in them
        # check for the if condition to see which is smaller
        while list1 != None and list2 != None:
            
            # if list 2 value is smaller, then add list 2 value
            # keep adding the value
            # if it is bigger than this value but smaller than the next 
            if list1.val >= list2.val: 

                # for the first element
                if head == ListNode(-1):
                    head = tail
                    tail = list2

                    # move list2
                    list2 = list2.next
                    continue

                print(f"adding value {list2.val} from list2 to {tail.val}")
                # shift the tail
                tail.next = list2
                tail = list2

                # shift list2
                list2 = list2.next

            # else add list 1 value
            else:
                # for the first element
                if head == ListNode(-1):
                    head = tail
                    tail = list2

                    # move list2
                    list2 = list2.next
                    continue

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
        return head.next

        # checking after everything if there is any in list1 or list2 left,
        # this will contain the largest values