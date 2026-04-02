from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # head is always moving
        curr = head
        temp_1 = None

        # as long as the head next is not none move the head
        while curr != None:

            print(f"adjusting the current node of {curr.val}")

            # retrieving for temp_2 before assining
            temp_2 = curr.next

            # reassign
            curr.next = temp_1

            # assigning temp_1 to be current
            temp_1 = curr

            # shift the current to be temp 2
            curr = temp_2
            
        return temp_1
        
    def view_link_list(self, head: Optional[ListNode]) -> Optional[ListNode]:

        print(head.val)

        curr = head

        while curr.next != None:

            curr = curr.next
            print(curr.val)