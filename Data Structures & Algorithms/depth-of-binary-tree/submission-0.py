# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Using BFS (breadth first search)
        queue = deque()

        if root:
            queue.append(root)

        
        level = 0

        while len(queue)>0:

            for _ in range(len(queue)):

                temp_node = queue.popleft()

                if temp_node.left:
                    queue.append(temp_node.left)
                
                if temp_node.right:
                    queue.append(temp_node.right)
            
            level+=1
        
        return level

            

