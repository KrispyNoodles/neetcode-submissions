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
        queue = deque()

        if root:
            queue.append(root)

        while len(queue)>=1:
            temp = []

            for _ in range(len(queue)):

                pop_node = queue.popleft()

                temp.append(pop_node.val)

                if pop_node.left:
                    queue.append(pop_node.left)

                if pop_node.right:
                    queue.append(pop_node.right)

            # append on the value on the right
            answer.append(temp[-1])
    
        return answer
        