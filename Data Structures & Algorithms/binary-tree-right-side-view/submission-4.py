# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        master_set = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue)>=1:

            temp = []

            for i in range(len(queue)):

                pop_node = queue.popleft()
                temp.append(pop_node.val)

                if pop_node.left:
                    queue.append(pop_node.left)

                if pop_node.right:
                    queue.append(pop_node.right)
            
            master_set.append(temp)

        answer = []
        for arrays in master_set:
            answer.append(arrays[-1])
    
        return answer
        