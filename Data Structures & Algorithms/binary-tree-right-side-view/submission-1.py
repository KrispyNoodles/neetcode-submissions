# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # getting each value in each layer then creating an answer array
        collectin_val = []
        queue = deque()

        if root:
            queue.append(root)
        
        while len(queue)>0:

            temp = []

            for _ in range(len(queue)):

                node = queue.popleft()
                temp.append(node.val)

                # it might have both left and right, elif means it has only either
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            collectin_val.append(temp)

        answer = []

        for arrays in collectin_val:
            answer.append(arrays[-1])

        return answer