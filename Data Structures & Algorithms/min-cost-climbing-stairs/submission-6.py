class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # create memo
        memo = [-1]*len(cost)

        def dfs(i):

            # when reach more than equal the len of the cost
            # might be more because +2
            if i>=len(cost):

                # return 0
                return 0

            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = min(cost[i]+dfs(i+1), cost[i]+dfs(i+2))

            return memo[i]

        return min(dfs(0), dfs(1))