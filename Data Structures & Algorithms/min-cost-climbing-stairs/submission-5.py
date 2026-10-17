class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # memoisation
        memo = [-1]*len(cost)

        def dfs(i):

            # can decide either to take 1 or 2 steps
            if i >= len(cost):
                return 0

            if memo[i] != -1:
                return memo[i]
                    
            # isit cheaper to add 2 or 1
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))

            return memo[i]

        return min(dfs(0), dfs(1))