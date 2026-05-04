# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        path = []

        def helperFn(root):

            if not root:
                return False

            # selecting the option
            path.append(root.val)

            # exploring other option

            if helperFn(root.left):
                return True
            if helperFn(root.right):
                return True
                
            # checking if it is at the lead node
            if not root.left and not root.right:

                if sum(path)==targetSum:
                    return True
                else:
                    path.pop()
                    return False

            path.pop()
            # after everything
            return False

        return helperFn(root)