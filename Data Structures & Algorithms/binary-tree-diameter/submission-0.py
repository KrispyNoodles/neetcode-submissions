# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diam = 0
        
        # creating a height function
        def helperFn(root):
            
            # when it hits the root, means it has reached a leaf node
            if not root:
                return 0
            
            left_height = helperFn(root.left)
            right_height = helperFn(root.right)

            height = max(left_height, right_height)+1

            # diameter == left_height + right_height
            diameter = left_height + right_height
            self.max_diam = max(self.max_diam, diameter)

            return height

        helperFn(root)
        return self.max_diam




            
            
