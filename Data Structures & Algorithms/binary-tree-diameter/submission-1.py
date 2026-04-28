
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # creating a variable
        self.max_diam = 0
        
        # creating a height function
        def helperFn(root):
            
            # when it hits the root, means it has reached a leaf node
            if not root:
                return 0
            
            l = helperFn(root.left)
            r = helperFn(root.right)

            # updating the max_diam
            self.max_diam = max(self.max_diam, l+r)
            
            return max(l,r)+1

        helperFn(root)
        return self.max_diam

# time complexity of O(n)