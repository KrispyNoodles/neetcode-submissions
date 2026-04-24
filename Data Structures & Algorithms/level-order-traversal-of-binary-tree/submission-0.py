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
        answer = []

        # if there is a root add it into the queue
        if root:
            queue.append(root)

        while len(queue)>0:

            temp_arr = []

            for _ in range(len(queue)):
                # pop left by FIFO rules and print it
                temp = queue.popleft()
                temp_arr.append(temp.val)
                print(temp.val)

                # if there is a value in temp left or right, add to queue
                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)
                

            # add it to answer
            answer.append(temp_arr)
        
        return answer

        