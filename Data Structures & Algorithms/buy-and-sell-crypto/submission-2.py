from typing import List

# Dynamic Programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # creating a buy int
        highest_earn = 0
    
        buy_price = prices[0]

        # assmign that I am selling every day
        # and my buy becomes the lowest price between the prev buy and the currently viewed price
        for sell in prices:

            # calculating and comparing with the current highest_earn value
            highest_earn = max(sell-buy_price, highest_earn)

            # updating the buy_price to be always the lowest
            # comparing between the previous buy and the current 
            buy_price = min(buy_price, sell)

        return highest_earn
    
# Therefore complexity is O(n) because of the for loop