# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## preorder moves root, then root.left, then right,
# then back up
# def preOrder(root):
#     if not root:
#         return

#     print(root.val)
#     preOrder(root.left)
#     preOrder(root.right)

## in order moves to the lowest of the left then slowly back up 
# def inOrder(root):
#     if not root:
#         return

#     inOrder(root.left)
#     print(root.val)
#     inOrder(root.right)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # recurssive method of using buildTreee, to buidl the root Node always

        # there is no value to build
        if not preorder:
            return None

        # retrieve the root to build
        root = TreeNode(preorder[0])

        # find where the root value is at in the inOrder
        root_pos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:root_pos+1], inorder[:root_pos])
        root.right = self.buildTree(preorder[1+root_pos:], inorder[root_pos+1:])

        return root

