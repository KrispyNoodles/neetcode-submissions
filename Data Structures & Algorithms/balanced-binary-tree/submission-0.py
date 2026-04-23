# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def postOrder(root):

            if not root:
                return 0

            left_height = postOrder(root.left)
            right_height = postOrder(root.right)

            # to pass on further back that one of the subtrees below is not balanced
            if left_height == -1 or right_height == -1:
                return -1
            
            # the first check to check if it is balanced
            if abs(left_height-right_height)>1:
                return -1

            height = max(left_height, right_height)+1

            return height

        ans = postOrder(root)
        
        if ans == -1:
            return False
        else:
            return True


    