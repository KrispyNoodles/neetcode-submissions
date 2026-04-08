class Solution:
    def calPoints(self, operations: List[str]) -> int:

        num_stack = []
        
        for char in operations:     

            # adding a score that is a sum of the prev two scores
            if char == '+':
                new_val = num_stack[-1] + num_stack[-2]
                num_stack.append(new_val)

            elif char == 'D':
                new_val = num_stack[-1]*2
                num_stack.append(new_val)

            elif char == 'C':
                num_stack.pop()
            # dont need check for numeric, as negative wont work and these are all the cases anyway
            else:
                num_stack.append(int(char))

        return sum(num_stack)

# time complexity of O(n)
# space of O(1)