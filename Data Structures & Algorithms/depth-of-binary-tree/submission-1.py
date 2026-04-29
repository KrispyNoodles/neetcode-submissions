# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # using BFS (Breadth First Search)
        queue = deque()
        answer = 0

        if root:
            queue.append(root)

        while len(queue)>=1:

            for _ in range(len(queue)):
                temp = queue.popleft()

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            answer+=1

        return answer

# time complexity of O(n) exploring each node once