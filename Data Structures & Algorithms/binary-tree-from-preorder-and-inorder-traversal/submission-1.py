# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # preorder, is starting from the root then going down one node at a time to the lowest leave
    # then moving down the root.right after (left, right)

    # inorder, is starting the from the element in the bottom left, right then moving up to the root, t
    # then moving down the deepest leave of the right side of the root and repeating the same for the left
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        # preorder's first value is always the root
        # creating the tree root
        root_val = preorder[0]
        root = TreeNode(root_val)
                
        # finding the index in the inorder
        index_root_val = inorder.index(root_val)

        # length of inorder and preorder is the same
        length_arr = len(inorder)

        # retrieving the left and right values to be added (inorder)
        left_nodes_in = inorder[0:index_root_val]
        right_nodes_in = inorder[index_root_val+1:length_arr]

        #retrieving the left and right values to be added (pre)
        left_nodes_pre = preorder[1:len(left_nodes_in)+1]
        right_nodes_pre = preorder[1+len(left_nodes_in):length_arr]


        # for everythin on the left and right, this has to be repeated
        # format for puttign in is, (preorder, inorder)
        root.left = self.buildTree(left_nodes_pre, left_nodes_in)
        root.right = self.buildTree(right_nodes_pre, right_nodes_in)

        return root