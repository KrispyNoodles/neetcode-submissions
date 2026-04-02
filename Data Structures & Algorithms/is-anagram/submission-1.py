# sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if length different reutn False, it defo wont match
        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True
        else:
            return False