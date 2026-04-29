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

            # selection
            path.append(root.val)

            # checking if it is leaf node
            if not root.left and not root.right:

                # check if fulfil condition
                if sum(path) == targetSum:
                    return True

                else:
                    path.pop()
                    return False
            
            # if either root.left and root.right is true dont need calculate
            if helperFn(root.left):
                return True
            if helperFn(root.right):
                return True
            
            # if all condition fails, just pop
            path.pop()

            return False

        return helperFn(root)

