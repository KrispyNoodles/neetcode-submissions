
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr != None:

            temp = curr

            curr = curr.next

            temp.next = prev

            prev = temp


        return prev
