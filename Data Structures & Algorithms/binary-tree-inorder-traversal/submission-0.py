# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        self.inOrder(root)
        
        return self.answer

    def inOrder(self, root):
        if not root:
            return

        self.inOrder(root.left)
        self.answer.append(root.val)
        self.inOrder(root.right)
        