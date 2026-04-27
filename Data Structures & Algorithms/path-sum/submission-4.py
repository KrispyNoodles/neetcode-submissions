# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # this keeps track of the path and pops it, if it doesnt work
        path = []

        def helperFunction(root):

            # if toort empty return False
            if not root:
                return False

            # adding the val into the path
            path.append(root.val)

            # it is a leaf node
            if not root.left and not root.right:
                if targetSum == sum(path):
                    return True
                else:
                    # pop it and return False
                    path.pop()
                    return False
            
            # checking down the left path, has an answer
            if helperFunction(root.left):
                return True

            if helperFunction(root.right):
                return True

            # after eveything does not fulfil
            path.pop()

            return False

        return helperFunction(root)



