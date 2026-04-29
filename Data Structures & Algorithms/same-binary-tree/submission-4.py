# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # checking if both dont have any more root
        if not p and not q:
            return True
        
        # if either still have
        if p and not q:
            return False

        if q and not p:
            return False
        
        # checking if values are the same
        if q.val != p.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)