# solved using recurrsion
# using a dict to prevent a recalculation
from collections import defaultdict

class Solution:

    # variable to store the values calculated before
    def_dict = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        
        # if n is 1 return 1 if n is 2 return 2
        if n<=2:
            return n
        
        if n in self.def_dict:
            return self.def_dict[n]
        
        # store the value into the dict
        self.def_dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # final_answer + 1 because of the last
        return self.def_dict[n]

# time complexity of O(n^2)
# space complectity of O(n)