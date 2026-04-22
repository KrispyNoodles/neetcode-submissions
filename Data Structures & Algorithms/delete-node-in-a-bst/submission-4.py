# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findMin(self, root):

        curr = root

        # checking if root and left avail
        while curr and curr.left:
            curr = curr.left

        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # if root emtpy return None, because nothing to delete
        if not root:
            return None

        # moving to the correct plcace to remove the node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            # checking if it has only left, right or both leaf nodes
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                # finding the smallest on the right
                new_root = self.findMin(root.right)

                # changing the root val
                root.val = new_root.val

                # removign the node
                root.right = self.deleteNode(root.right, root.val)

        return root

