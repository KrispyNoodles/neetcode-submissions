# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    # finding the minimum value
    def minNode(self, root):

        curr = root

        # as long as curr is not None and there is a curr.left, move down the left path
        while curr and curr.left:
            curr = curr.left
        
        return curr

    # deleting node function
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root: 
            return None

        # trying to find the value
        if key> root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key< root.val:
            root.left = self.deleteNode(root.left, key) 
        
        # found the value time to delete it
        else:

            # if there is no more leafs on the left, return the right
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                # find the smallest node on the right side to be ready to replace
                smallest_node = self.minNode(root.right)

                # replacing
                root.val = smallest_node.val

                # removing teh duplicated node
                root.right = self.deleteNode(root.right, root.val)
                
        return root


