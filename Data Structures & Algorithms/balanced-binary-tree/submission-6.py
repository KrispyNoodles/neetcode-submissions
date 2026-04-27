# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def helper_fn(root):

            if not root:
                return 0

            len_left = helper_fn(root.left)
            len_right = helper_fn(root.right)

            # getting height
            height = max(len_left, len_right)+1

            # checking if either is exceding 1
            if abs(len_left-len_right)>1:
                return -1
            
            if len_left==-1 or len_right==-1:
                return -1

            return height
            
        ans = helper_fn(root)
        
        return helper_fn(root)!=-1


            
        
