# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def heightFn(root):

            if not root:
                return 0

            # getting height
            left_height = heightFn(root.left)
            right_height = heightFn(root.right)

            # if either if -1 return -1
            if left_height == -1 or right_height==-1:
                return -1
            
            # condition check
            if abs(left_height-right_height)>1:
                return -1

            height = max(left_height, right_height) + 1

            return height

        return heightFn(root) != -1
