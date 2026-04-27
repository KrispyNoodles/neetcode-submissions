# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        if root:
            queue.append(root)
        
        answer = []

        while len(queue)>0:

            temp = []

            for _ in range(len(queue)):

                # pop it from the queue
                node = queue.popleft()
                temp.append(node.val)

                # checking if i has root left or right
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            answer.append(temp)
        
        return answer
