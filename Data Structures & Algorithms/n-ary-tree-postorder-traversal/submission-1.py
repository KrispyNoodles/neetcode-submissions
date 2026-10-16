"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        answer = []

        # dfs
        def dfs(root):
            if not root:
                return

            # move through all children
            for children in root.children:
                dfs(children)
            answer.append(root.val)
        
        dfs(root)
        return answer