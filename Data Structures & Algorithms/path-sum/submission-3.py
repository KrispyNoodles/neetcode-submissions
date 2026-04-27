# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # if not root, means it is empty
        if not root:
            return False

        # if there is no more root left or root right, it means it is a leaf node
        if not root.left and not root.right:

            # check if the current value is the same as the targetSum:
            if root.val == targetSum:
                return True

            else:
                return False
        
        # else subtract the root.val from the targetsum
        targetSum = targetSum-root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
