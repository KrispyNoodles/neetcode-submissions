from typing import List

# using two pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # creating a buy int
        highest_earn = 0
        
        # these are index pointers that hold 
        l = 0 # buy
        r = 0 # sell

        for index in range(len(prices)):

            # the right value slowly increments across the len of the array
            r = index

            # if the left value is more than the right,
            # this means I am buying at a higher prices than the one being sold for
            # then left value becomes the right
            if prices[l] > prices[r]:
                l = r

            # buy - sell
            earn = prices[r] - prices[l]

            # checkinf if it is higher than the current highest_earning
            if earn > highest_earn:
                highest_earn = earn
        
        return highest_earn            
    
# Therefore complexity is O(n) because of the for loop