# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return
        
        # for every preorder and inorder, we can create a node and traverse the left and right of it

        # build the tree, connect the left and right
        new_node = TreeNode(preorder[0])

        # find where 1 is at and everything on the left
        root_index = inorder.index(preorder[0])
        new_l_in = inorder[0:root_index]
        # new pre_left and new inorder_left
        new_l_p = preorder[1:1+len(new_l_in)]

        # build left and build right
        new_node.left = self.buildTree(new_l_p, new_l_in)

        # # new pre_right and new inorder_right
        new_r_in = inorder[root_index+1:]
        # new pre_left and new inorder_left
        new_r_p = preorder[1+len(new_l_in):]
        
        new_node.right = self.buildTree(new_r_p, new_r_in)

        return new_node

        