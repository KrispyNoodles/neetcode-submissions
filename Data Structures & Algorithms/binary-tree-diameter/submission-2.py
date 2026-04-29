# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # recurssively finding the max(left + height), because that is the diameters across the nodes
        max_diam = 0

        def helperFn(root):
            nonlocal max_diam
            
            if not root:
                return 0
            
            left_height = helperFn(root.left)
            right_height = helperFn(root.right)

            height = max(left_height, right_height)+1
            max_diam = max(max_diam, left_height+right_height)

            return height
        helperFn(root)

        return max_diam



        