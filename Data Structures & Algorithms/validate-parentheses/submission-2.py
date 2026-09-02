class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        left = 0
        right = len(s)-1

        for i in range(len(s)):

            # if i is an open
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                stack.append(s[i])
            
            # pop the val from the stack and see which one it matches
            else:

                # checking if stack is empty, if it is then return false
                if stack == []:
                    return False
                pop_val = stack.pop()

                if pop_val == '[':
                    # checking if the current val is the oppposite
                    if s[i]==']':
                        continue
                    else:
                        return False
            
                if pop_val == '{':
                    # checking if the current val is the oppposite
                    if s[i]=='}':
                        continue
                    else:
                        return False
            
                if pop_val == '(':
                    # checking if the current val is the oppposite
                    if s[i]==')':
                        continue
                    else:
                        return False
            
        # unmatched pairs in the stack
        if stack != []:
            return False
        
        else:
            return True