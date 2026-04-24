# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper_fn(root):
            
            # if there is no root return 0
            # becuase it means that it is balanced
            if not root:
                return 0

            height_left = helper_fn(root.left)
            height_right = helper_fn(root.right)

            # if either root.left or root.right is -1, it means the subtree below has already been off balanced
            if height_left==-1 or height_right==-1:
                return -1

            # condition of when the tree is off balanced
            if abs(height_left-height_right)>1:
                return -1
            
            # height is finding the max of either and increasing by 1
            height = max(height_left, height_right)+1
            
            return height

        return helper_fn(root)!=-1
