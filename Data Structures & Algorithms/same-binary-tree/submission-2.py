# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # it has reached the leaf
        # (this checks that both are None)
        if not p and not q:
            return True
        
        # if either is None 
        # has to be done before val because it will check none
        if not p or not q:
            return False

        # the values they have are differnet
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# time compelxity of O(n), since it will check all nodes