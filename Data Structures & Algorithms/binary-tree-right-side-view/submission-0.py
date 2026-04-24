# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # when moving right then append to the answer
        total_arr = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue)>=1:

            temp_arr = []
            for _ in range(len(queue)):
                temp = queue.popleft()
                temp_arr.append(temp.val)

                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

            total_arr.append(temp_arr)

        # for all answer in the height, retrieve the right end
        answer = []

        for arrays in total_arr:
            answer.append(arrays[-1])

        return answer
        