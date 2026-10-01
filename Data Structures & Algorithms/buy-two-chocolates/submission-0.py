class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        # retrieve the two lowest
        prices.sort()

        cheapest = prices[:2]

        left = money-sum(cheapest)

        if left>=0:
            return left

        else:
            return money