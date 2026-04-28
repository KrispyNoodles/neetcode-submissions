# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helperFunction(root):

            if not root:
                return 0

            len_left = helperFunction(root.left)
            len_right = helperFunction(root.right)

            if len_left == -1 or len_right == -1:
                return -1
            
            if abs(len_left-len_right)>1:
                return -1

            length = max(len_left, len_right)+1

            return length

        return helperFunction(root)!=-1
        