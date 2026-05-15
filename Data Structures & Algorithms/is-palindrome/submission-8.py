# using two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1

        while right>left:

            # convert both to lower
            left_char = s[left].lower()
            right_char = s[right].lower()

            # if either is not then shift
            if not left_char.isalnum():
                left+=1
            
            if not right_char.isalnum():
                right-=1

            # checking if it is alphanumeric
            if left_char.isalnum() and right_char.isalnum():

                # check if they are the same
                if left_char!=right_char:
                    return False

                left+=1
                right-=1

        return True
        