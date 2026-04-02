# using divide and conquer method
from typing import List

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # edge case of none
        if not lists:
            return None
        
        else:
            return self.divide(lists, 0, len(lists)-1)
        
    
    # the lists, the left and right index
    def divide(self, lists, l, r):

        # the index of left has move across the right
        if l > r:
            return None
        
        # there is only one elemnt?
        if l==r:
            return lists[l]
        
        mid = (l+(r-1))//2

        # calculate left
        left = self.divide(lists, l, mid)

        # calculate right
        right = self.divide(lists, mid+1, r)

        # return 
        return self.conquer(left, right)
    

    # conquer is a normal merge between two lists
    def conquer(self, l1, r1):

        dummy_node = ListNode(-1)
        tail = dummy_node

        # as long as list1 and list2 are not empty
        while l1 and r1:  

            # checking if which value is bigger
            if l1.val >= r1.val:

                # list2 becomes the new tail
                tail.next = r1

                # shift list2
                r1 = r1.next
            
            else:
                tail.next = l1
                l1 = l1.next

            # change the new tail
            tail = tail.next
    
        # checking if either is left
        if l1:
            tail.next = l1
        if r1:
            tail.next = r1

        return dummy_node.next