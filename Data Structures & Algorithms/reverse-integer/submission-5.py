# top tier Brute Force
class Solution:
    def reverse(self, x: int) -> int:
        
        value = x
        x = abs(x)

        # flipping the result
        result = int(str(x)[::-1])

        if value<0:
            result = -result

        # checking if within boundaries
        if result > (1<<31) -1 or result < -(1<<31):
            return 0

        else:
            return result

# time complexity of O(1)
# space complexity of O(1)