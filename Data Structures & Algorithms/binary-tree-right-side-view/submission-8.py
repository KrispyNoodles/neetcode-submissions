# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()

        if root:
            queue.append(root)

        answer = []
        
        while queue:

            queue_len = len(queue)

            for i in range(queue_len):

                pop_root = queue.popleft()

                if pop_root.left:
                    queue.append(pop_root.left)

                if pop_root.right:
                    queue.append(pop_root.right)
                
                if i == queue_len-1:
                    answer.append(pop_root.val)

        return answer
