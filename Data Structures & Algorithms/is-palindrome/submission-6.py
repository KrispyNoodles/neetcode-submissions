class Solution:
    def isPalindrome(self, s: str) -> bool:

        # convert all to small caps
        temp_str = ""

        # looping through cha
        for characters in s:

            # checking if it is an alphanumeric number
            if characters.isalnum():

                # convert into lower
                temp_str += characters.lower()

        # logic here is the same
        if temp_str == temp_str[::-1]:
            return True
        else:
            return False
        
# Time Computation complxity of O(N) because there is only one loop that goes through all the characters of s