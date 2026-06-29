# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        collector = []
        
        # helper fn
        def helper_fn(root):
            if not root:
                return

            helper_fn(root.left)
            collector.append(root.val)
            helper_fn(root.right)
        
        helper_fn(root)
        return collector