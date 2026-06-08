# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # collect all the values then return

        answer = []
        queue = deque()

        # using a stack to pop left
        if root:
            queue.append(root)

        # keep poping left
        while len(queue)>0:

            for _ in range(len(queue)):
                pop_node = queue.popleft()
                print(pop_node.val)

                # checking left and right
                if pop_node.left:
                    queue.append(pop_node.left)
                
                if pop_node.right:
                    queue.append(pop_node.right)
            answer.append(pop_node.val)
        return answer