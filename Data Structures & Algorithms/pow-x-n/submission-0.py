# neetcode soln
class Solution:
    def myPow(self, x: float, n: int) -> float:

        # creating a power function to solve only positive
        def helper(x, n):

            # create the base cases
            if n == 1:
                return x
            
            elif n == 0:
                return 1
            
            # you just do the calulcation for odd or even fist
            res = helper(x, n//2)

            # multiply by itseld
            res = res * res

            # the odd can be adjusted in here
            if n%2==0:
                return res
            else:
                # adding one more x here
                return res*x
            
        result = helper(x, abs(n))

        if n >0:
            return result
        
        else:
            return 1/result