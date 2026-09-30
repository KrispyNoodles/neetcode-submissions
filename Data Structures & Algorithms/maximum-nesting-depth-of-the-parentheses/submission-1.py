class Solution:
    def maxDepth(self, s: str) -> int:
        
        # just have a stack
        stack = []
        answer = 0

        # we take note how big this stack if everytime we find a value
        for char in s:

            answer = max(answer, len(stack))
            if char == '(':
                stack.append('(')
            
            elif char == ')':
                pop_val = stack.pop()

        return answer
