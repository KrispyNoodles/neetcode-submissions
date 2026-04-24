# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # finding the smallest value
        def findMin(root):

            temp = root

            while temp and temp.left:
                temp=temp.left

            return temp

        # if there is nothing to delete dont need delete LOL?
        if not root:
            return None
        
        # finding the position of where to delete
        if key>root.val:
            root.right = self.deleteNode(root.right,key)

        elif key<root.val:
            root.left = self.deleteNode(root.left,key)

        else:
            # checking if either left or right empty then can just return those, no need further steps done
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # find the min, of the right subtree to replace with the current root
                min_val = findMin(root.right)
                root.val = min_val.val
                # remove the duplicated min_val node
                root.right = self.deleteNode(root.right, root.val)

        return root


