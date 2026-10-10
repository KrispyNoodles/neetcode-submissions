class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # creating a memo list
        memo = [-1]*len(cost)

        def dfs(i):

            # we have reached the end of the stair case
            if i>=len(cost):
                return 0
            
            # if it is inside the memo, return it
            if memo[i]!=-1:
                return memo[i]

            # either take 1 or 2 steps
            memo[i] = cost[i]+min(dfs(i+1), dfs(i+2))

            return memo[i]
        
        return min(dfs(0), dfs(1))