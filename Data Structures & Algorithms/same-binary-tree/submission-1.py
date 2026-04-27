# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # it has ended the same time (checking for structure)
        if not p and not q:
            return True

        # one is None and the other is not (both None handled above)        
        if not p or not q:
            return False

        # (checking for value)
        if q.val != p.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 