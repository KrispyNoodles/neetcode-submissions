# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # if the root is empty it means it has found the correct place to create the treenode
        if not root:
            return TreeNode(val)

        # if not recurssive fn
        if val > root.val:
            # move down the right side
            root.right = self.insertIntoBST(root.right, val)

        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root