class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        # retrieve the two lowest
        prices.sort()

        left = money-prices[0]-prices[1]

        if left>=0:
            return left

        else:
            return money