# Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<=1:
            return n
        
        # create a temp cache with the len of 2, since you only need the previous 2 to calculate
        dp_array = [1,2]
        i = 3

        while i<=n:

            # do the switcheroo
            # update 0 to be 1
            # and update 1 to be 0+1
            dp_array[0], dp_array[1] = dp_array[1], dp_array[0]+dp_array[1]

            i+=1
    
        return dp_array[1]

# time complexity O(n)