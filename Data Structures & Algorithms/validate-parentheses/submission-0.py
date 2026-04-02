class Solution:
    def isValid(self, s: str) -> bool:
        
        # creating a stack
        open_stack = []

        close_brackets_set = {')','}',']'}

        for character in s:
            
            # if current character in set
            # and there is was a closer bracket appended
            if character in close_brackets_set:
                if open_stack:
                    # case for all
                    pop_brack = open_stack.pop()

                    # if the character is ']', the pop value is expected to be '['
                    if character == ']' and pop_brack != '[':
                        return False
                    # same for other cases
                    if character == '}' and pop_brack != '{':
                        return False
                    
                    if character == ')' and pop_brack != '(':
                        return False
                # this means a closed bracket was found without an open
                else:
                    return False

            else:
                open_stack.append(character)

        # if after all that shit still got a bracket that has been match
        # it means it is not matched correctly
        if open_stack:
            return False
        else:
            return True
