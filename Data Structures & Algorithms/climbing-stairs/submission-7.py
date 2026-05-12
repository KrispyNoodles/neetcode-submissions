class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<=2:
            return n
        
        # create a temp cache with the len of 2, since you only need the previous 2 to calculate       
        n_minus2 = 1
        n_minus1 = 2

        # start at 3 because we are now solving for the 3rd solution
        # and solve till n+1 as range doesnt include the last value
        for _ in range(3, n+1):

            # do the switcheroo
            # update 0 to be 1
            # and update 1 to be 0+1
            n_minus2, n_minus1 = n_minus1, n_minus1+n_minus2

        return n_minus1