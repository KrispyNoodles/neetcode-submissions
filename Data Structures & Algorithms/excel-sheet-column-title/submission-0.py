class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = []

        while columnNumber > 0:

            # decrease the number
            columnNumber -= 1

            # how far is it from A
            offset = columnNumber%26
            res += chr(ord('A') + offset)
            columnNumber //=26
        
        return ''.join(reversed(res))
            