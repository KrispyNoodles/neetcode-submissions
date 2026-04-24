# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer = []

        # inorder
        def helperFn(root, answer):
            if not root:
                return

            # move down the left all the way then up then right
            helperFn(root.left, answer)
            print(root.val)
            answer.append(root.val)
            helperFn(root.right, answer)
        
        helperFn(root, answer)
        return answer
        