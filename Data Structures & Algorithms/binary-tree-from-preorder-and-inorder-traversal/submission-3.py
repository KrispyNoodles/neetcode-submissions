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
        root_val = preorder[0]
        root = TreeNode(root_val)

        # find where the root value is at in the inOrder
        root_pos = inorder.index(root_val)

        # creating temp arrays to populate the root.left and root.right

        # inOrder
        root_left_in = inorder[:root_pos]
        root_right_in = inorder[root_pos+1:]

        # pre
        # getting length of 1
        temp_val = len(root_left_in)
        root_left_pre = preorder[1:temp_val+1]
        root_right_pre = preorder[1+temp_val:]

        root.left = self.buildTree(root_left_pre, root_left_in)
        root.right = self.buildTree(root_right_pre, root_right_in)

        return root

