class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # rearrange both arrays then compare
        if sorted(s) == sorted(t):
            return True

        else:
            return False