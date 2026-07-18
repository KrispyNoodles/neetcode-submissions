class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1

        while right>left:

            # continue shifting left/right if not alnum
            while not s[left].isalnum() and right>left:
                left+=1
            
            while not s[right].isalnum() and right>left:
                right-=1
            
            # if both are 
            if s[left].lower()==s[right].lower():
                left+=1
                right-=1

            else:
                return False
        
        return True