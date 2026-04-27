# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer = []
        
        # depth first then back up
        def helper(root):
            if not root:
                return

            helper(root.left)
            answer.append(root.val)
            helper(root.right)

        helper(root)
        return answer