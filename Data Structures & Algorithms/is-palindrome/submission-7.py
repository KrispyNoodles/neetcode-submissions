class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # removing all ""
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string+=char.lower()

        # checkinf if the flip is the same
        # flip_string = 

        if new_string == new_string[::-1]:
            return True
        else:
            return False
