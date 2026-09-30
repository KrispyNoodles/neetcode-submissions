# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # checking if it is balance
        def height(root):

            # if there is no root
            if not root:
                return 0

            # if either is false then return false alreadyu
            left_height = height(root.left)
            right_height = height(root.right)

            # if either if false then return false
            if left_height == -1 or right_height== -1:
                return -1

            if abs(right_height-left_height)>1:
                return -1

            # return the height of both side +1
            return max(left_height, right_height)+1
        
        if height(root)==-1:
            return False

        else:
            return True