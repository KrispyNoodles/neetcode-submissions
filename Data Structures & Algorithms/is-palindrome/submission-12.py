class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while right>left:
            print(s[left])
            print(s[right])

            if not s[left].isalnum():
                left+=1
            
            if not s[right].isalnum():
                right-=1
            
            if s[left].isalnum() and s[right].isalnum():

                # do comparison
                if s[left].lower() == s[right].lower():
                    left+=1
                    right-=1
                else:
                    return False

        return True