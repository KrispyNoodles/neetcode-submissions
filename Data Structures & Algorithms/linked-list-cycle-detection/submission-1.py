class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # creating a list to store all the nodes that you have visited
        # if the node is the same, congrats you are in a cycle

        slow, fast = head, head

        # ensuring that the fast has a next
        while fast and fast.next:

            # move the slow and fast
            # fast loops within the cycle and eventually catches slow
            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                return True
        
        # else it exists the loop and return False
        return False

# time complexity of O(n)
# space complexity of O(1)