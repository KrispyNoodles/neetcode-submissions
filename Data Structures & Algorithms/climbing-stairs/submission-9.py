class Solution:
    def climbStairs(self, n: int) -> int:
        

        # creating a dict that stores all possible answers
        c_dict = {0:1, 1:1}

        for i in range(1,n):
            
            # retrieve the previous two steps
            now = c_dict[i-1] + c_dict[i]

            c_dict[i+1] = now
        
        return c_dict[n]
