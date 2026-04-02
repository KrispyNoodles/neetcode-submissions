# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        high = 2**31-1
        low = 0

        while high>=low:
            middle = (high+low)//2

            # this means the guess is too high
            if guess(middle) == -1:
                high = middle-1

            elif guess(middle) == 1:
                low = middle+1
            
            # number found
            else:
                return middle