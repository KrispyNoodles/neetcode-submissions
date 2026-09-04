class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        buy = prices[0]
        profit = 0

        for sell in prices:

            # update the max
            profit = max(profit, sell-buy)

            # update the min, compare previous low buy and current sell
            buy = min(buy, sell)

        return profit
