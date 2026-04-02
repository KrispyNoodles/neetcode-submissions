class Solution:
    def isValid(self, s: str) -> bool:

        stack_char = []

        closed_brack_set = {'}', ']', ')'}

        
        for character in s:

            # the idea is to alwasy clear the stack_char
            # if by the end there is still a value in the stack it means it isnt matched correctly
            if stack_char and character in closed_brack_set:

                # trying to match the chracter brackets
                # and checking if the one poped is not the same
                # then return false
                pop_char = stack_char.pop()
                
                if character == '}' and pop_char != '{':
                    
                    return False
                
                if character == ']' and pop_char != '[':
                    
                    return False

                if character == ')' and pop_char != '(':
                    return False

            else:
                stack_char.append(character)

        # else check if there is anything in the stack still
        if not stack_char:
            return True
        
        else:
            return False