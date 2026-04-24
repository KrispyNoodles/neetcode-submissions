# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# using DFS (Depth First Search)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        # this means it is the leaf node
        if not root.left and not root.right:

            # check if the last value is the same as the targetSum
            if (targetSum-root.val)==0:
                return True

            else:
                return False

        # subtracting the tragetSum from the current node it is at if it is not the leaf node
        targetSum-=root.val
        
        # recurssive call
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum) 
