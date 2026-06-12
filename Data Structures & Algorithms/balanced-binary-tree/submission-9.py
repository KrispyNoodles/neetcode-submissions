# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def heightFn(root):

            # if there is not root, the height is 0
            if not root:
                return 0

            # getting left and right side
            left_height = heightFn(root.left)
            right_height = heightFn(root.right)
            
            # checking if either side has a height difference more than 1
            if abs(right_height-left_height)>1:
                return -1

            # checking if either had alreayd reached -1 
            if left_height == -1 or right_height==-1:
                return -1

            # calculating heigh
            height = max(left_height, right_height)+1

            return height
        
        return heightFn(root)!=-1