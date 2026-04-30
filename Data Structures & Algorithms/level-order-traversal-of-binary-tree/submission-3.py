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

        if not root:
            return []
        else:
            queue.append(root)

        answer = []

        while len(queue)>=1:

            new_row = []

            for _ in range(len(queue)):

                temp_node = queue.popleft()
                new_row.append(temp_node.val)

                if temp_node.left:
                    queue.append(temp_node.left)

                if temp_node.right:
                    queue.append(temp_node.right)

            answer.append(new_row)

        return answer

        
