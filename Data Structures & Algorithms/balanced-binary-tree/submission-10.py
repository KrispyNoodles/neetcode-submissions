# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helperFn(root):

            if not root:
                return 0

            # calculating height of left
            leftHeight = helperFn(root.left)

            rightHeight = helperFn(root.right)

            # checking if either is more than 1
            if abs(rightHeight-leftHeight)>1:
                return -1

            
            # if either -1 pass it on
            if rightHeight ==-1 or leftHeight==-1:
                return -1

            # calculation of height
            new_height = max(rightHeight, leftHeight)+1

            return new_height


        if helperFn(root)==-1:
            return False

        return True
