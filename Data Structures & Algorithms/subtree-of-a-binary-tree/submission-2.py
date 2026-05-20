from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # use dfs and see if it is inside

        collector = []

        # preorder dfs as it shows the root
        def dfs(root):

            # to ensure the roots are added
            if not root:

                # to check that it is a root
                collector.append('#')
                return

            collector.append(f'"{root.val}"')
            dfs(root.left)
            dfs(root.right)
            
        # collect left
        dfs(root)
        collector_root = collector.copy()

        # reset to collect the right_side
        collector=[]
        dfs(subRoot)

        # join both of them together
        root_string = "".join(collector_root)
        subroot_string = "".join(collector)

        # check if at the front or at the back
        if subroot_string in root_string:
            return True

        return False
