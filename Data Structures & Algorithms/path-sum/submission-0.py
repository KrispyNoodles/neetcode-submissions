# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # find all the path and add along
        # sum them, then check if the target sum is reached
        sum_val = 0

        path = []

        def canReachLeaf(root):

            if not root:
                return False

            path.append(root.val)

            # check that it is a leaf node to see if the path is correct
            if not root.right and not root.left:

                if sum(path)!=targetSum:
                    path.pop()
                    return False
                else:
                    return True

            if canReachLeaf(root.left):
                return True
        
            if canReachLeaf(root.right):
                return True

            # pop when it cant fulfil the condition
            path.pop()
            return False

        print(path)
        return canReachLeaf(root)
        
        