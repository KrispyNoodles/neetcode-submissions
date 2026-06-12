# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = []

        # creating a queue
        que = deque()

        if root:
            que.append(root)

        while que:
            temp = []
            for _ in range(len(que)):

                pop_node = que.popleft()
                temp.append(pop_node.val)

                # checking if pop_node have left or right leaves
                if pop_node.left:
                    que.append(pop_node.left)
                
                if pop_node.right:
                    que.append(pop_node.right)

            # add it to the answer
            answer.append(temp)

        return answer
