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

        while queue:

            temp = []

            for _ in range(len(queue)):

                pop_root = queue.popleft()
                temp.append(pop_root.val)

                if pop_root.left:
                    queue.append(pop_root.left)
                
                if pop_root.right:
                    queue.append(pop_root.right)

            answer.append(temp)

        return answer