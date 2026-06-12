# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        # using DFS
        def helperFn(root):

            if not root:
                return

            helperFn(root.left)
            answer.append(root.val)
            helperFn(root.right)

        helperFn(root)
        return answer