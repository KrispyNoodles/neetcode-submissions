# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        answer = []
        
        # retrieve the value then return
        # because it is a proper BST
        def helper_fn(root):

            if not root:
                return

            helper_fn(root.left)
            answer.append(root.val)
            helper_fn(root.right)

        helper_fn(root)

        return answer[k-1]
