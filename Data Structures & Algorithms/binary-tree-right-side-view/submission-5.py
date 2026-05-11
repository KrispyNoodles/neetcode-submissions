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

            length_queue = len(queue)
            for i in range(len(queue)):

                pop_node = queue.popleft()

                # appending only the last val
                if i==length_queue-1:
                    answer.append(pop_node.val)

                if pop_node.left:
                    queue.append(pop_node.left)
                
                if pop_node.right:
                    queue.append(pop_node.right)

        return answer
                

        