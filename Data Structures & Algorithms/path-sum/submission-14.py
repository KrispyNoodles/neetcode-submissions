# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # variation of my work
        
        def dfs(root, count):
            
            # if the end reutn 0
            if not root:
                return False

            # add the value
            count+=root.val

            # checking if it is a leaf
            if not root.left and not root.right:
                
                if count==targetSum:
                    return True
                else:
                    return False

            # explore left and right
            if dfs(root.left, count) or dfs(root.right, count):
                return True
            else:
                return False

        return dfs(root, 0)