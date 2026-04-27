# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def preorder(root):
    # if not root:
    #     reutrn
    # print(root.val)
    # preorder(root.left)
    # preorder(root.right)

# def inorder(root):
    # if not root:
    #     reutrn
    # inorder(root.left)
    # print(root.val)
    # inorder(root.right)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        # the first val in the preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # finding the position in the inorder
        root_pos = inorder.index(root_val)
        
        left_preorder = preorder[1:1+root_pos]
        right_preorder = preorder[1+root_pos:]

        left_inorder = inorder[0:root_pos]
        right_inorder = inorder[root_pos+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

        