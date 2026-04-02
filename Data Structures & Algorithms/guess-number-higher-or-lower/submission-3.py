class Solution:
    def guessNumber(self, n: int) -> int:

        high = n
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