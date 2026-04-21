# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # creating a function that searches for the biggest element on the left
    def findBig(self, root):

        curr = root

        # while there is curr and there is an element on the right, move to it
        while curr and curr.right:
            curr = curr.right

        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # if empty return nothing to delete
        if not root:
            return None

        # finding the elment to delete
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:
            # checking if the left or right is empty, easy to work with
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                # retrieving the element, replacing, then removing the duplicated val at the leaf
                large_left = self.findBig(root.left)
                root.val = large_left.val
                
                root.left = self.deleteNode(root.left, root.val)

        return root

        