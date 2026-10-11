class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [-1]*len(cost)

        def dfs(i):

            # when reaches top of stair case
            if i>=len(cost):
                return 0

            # if found inside the memo
            if memo[i]!=-1:
                return memo[i]
            
            # elese calculate the memo
            # either take 1 or 2 steps
            # at the current step isit cheaper to move 1 or two
            memo[i] = cost[i] + min((dfs(i+1), dfs(i+2)))

            return memo[i]
        
        # not sure if 0 or 1 step at first is the best
        return min(dfs(0), dfs(1))