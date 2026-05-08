# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        arr = []
        
        # traverse to the furthest left
        def helperFn(root):

            if not root:
                return

            helperFn(root.left)
            arr.append(root.val)
            helperFn(root.right)

        helperFn(root)
        return arr[k-1]