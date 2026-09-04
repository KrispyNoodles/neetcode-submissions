class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # creating a temp array for all values
        # O(n^2) soln

        answer = 0

        for i in range(len(prices)):

            buy = prices[i]

            # print(prices[i:len(prices)])

            for sell in prices[i:len(prices)]:
                answer = max(answer,(sell-buy))
                print(answer)

        return answer


