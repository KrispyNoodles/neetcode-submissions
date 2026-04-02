class Solution:
    def climbStairs(self, n: int) -> int:
        
        # if n is 1 return 1 if n is 2 return 2
        if n<=2:
            return n
        
        # final_answer + 1 because of the last
        return self.climbStairs(n-1) + self.climbStairs(n-2)

        
