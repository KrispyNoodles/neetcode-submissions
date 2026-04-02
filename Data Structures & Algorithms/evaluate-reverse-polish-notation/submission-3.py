from typing import List

# my soln
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # creating a stack for the num

        num_stack = []

        for char in tokens:
            
            if char == '+':

                # pop the last two values and add them 
                num_1 = num_stack.pop()
                num_2 = num_stack.pop()

                # together then throw back to the stack
                value = num_1 + num_2
                num_stack.append(value)

            elif char == '-':

                # pop the last two values and add them 
                num_1 = num_stack.pop()
                num_2 = num_stack.pop()

                # together then throw back to the stack
                value = num_2 - num_1
                num_stack.append(value)

            elif char == '*':

                print('times found')

                # pop the last two values and add them 
                num_1 = num_stack.pop()
                num_2 = num_stack.pop()

                # together then throw back to the stack
                value = num_1 * num_2

                num_stack.append(value)
            
            elif char == '/':

                # pop the last two values and add them 
                num_1 = num_stack.pop()
                num_2 = num_stack.pop()

                # together then throw back to the stack
                value = num_2 / num_1
                num_stack.append(int(value))

            # appending only numeric numbers
            # cant use .isnumeric() and isdigit() since they cant pick up negative values
            else:
                # convert into int
                num_stack.append(int(char))

        # return the last and supposedly only value in the stack
        return num_stack[-1]
        