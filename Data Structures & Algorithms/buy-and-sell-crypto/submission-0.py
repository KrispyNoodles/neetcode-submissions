class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # creating a buy int
        highest_earn = 0

        for index in range(len(prices)):

            buy = prices[index]

            # creating
            sold = max(prices[index:])

            earn = sold-buy

            if earn>=highest_earn:
                highest_earn=earn

        return highest_earn
