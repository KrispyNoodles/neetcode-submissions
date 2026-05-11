# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # retrieve the values in order, then return the 1-index value of the tree
        collect_val = []

        def helperFn(root):

            if not root:
                return

            helperFn(root.left)
            collect_val.append(root.val)
            helperFn(root.right)

        helperFn(root)
        # 0 index become 1, 
        # so everything in k to become 0-index is -1?
        return collect_val[k-1]