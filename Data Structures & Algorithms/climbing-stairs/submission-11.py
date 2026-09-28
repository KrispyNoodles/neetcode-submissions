class Solution:
    def climbStairs(self, n: int) -> int:
        
        # handling base case
        if n<=2:
            return n
        
        # the possible combination when n is 2 and is 1
        curr_step = 2
        prev_step = 1

        for _ in range(2,n):
            next_step = curr_step + prev_step

            # the next round, the new prev step will be the curr step
            prev_step = curr_step
            
            # and the curr_step will be the next_step
            curr_step = next_step

        return next_step
