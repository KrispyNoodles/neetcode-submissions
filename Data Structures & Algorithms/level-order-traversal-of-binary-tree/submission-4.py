# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # using BFS
        master_set = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue)>=1:

            temp_arr = []

            for _ in range(len(queue)):

                curr_node = queue.popleft()
                temp_arr.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)


            master_set.append(temp_arr)


        return master_set


