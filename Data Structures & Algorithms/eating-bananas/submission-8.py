from typing import List
from math import ceil

# TLE
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # if the len of h is == piles than 
        # return max number of bananes in the single pile
        if len(piles) == h:
            return max(piles)

        # range of speed eating is 
        return self.helper_function(1, max(piles), piles, h)


    # similar to previous function of earlier True version
    # [1,2,3,4,5]
    # # the range represents the different speed timing 
    def helper_function(self, low, high, piles, h):

        if low>high:
            return low
        
        middle = (low+high)//2

        # can afford to move the middle-1
        if self.checker_function(middle, piles, h):
            return self.helper_function(low, middle-1, piles, h)
        
        else:
            return self.helper_function(middle+1, high, piles, h)        
    
    # a function to check if it fulfils the condition
    #
    def checker_function(self, proposed_speed, piles, h):

        total_hour = 0

        for bananas in piles:

            total_hour += ceil(bananas/proposed_speed)


        # checker for h
        if h<total_hour:
            return False
        
        else:
            return True