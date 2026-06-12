# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []

        que = deque()

        # creating a que
        if root:
            que.append(root)

        while que:

            # getting the range here
            length_que = len(que)

            for i in range(len(que)):

                pop_node = que.popleft()

                if i == length_que-1:
                    answer.append(pop_node.val)

                if pop_node.left:
                    que.append(pop_node.left)

                if pop_node.right:
                    que.append(pop_node.right)

        return answer