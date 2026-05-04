# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        temp_array = []

        def helperFn(root):

            if not root:
                return

            helperFn(root.left)
            temp_array.append(root.val)
            helperFn(root.right)
        
        helperFn(root)
        return temp_array