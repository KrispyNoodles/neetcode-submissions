class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # I can choose either to take 1 or two steps
        memo = [-1]*len(cost)

        def dfs(i):

            # if I have reached the end return
            if i>=len(cost):
                return 0

            # if answer in the memo return 
            if memo[i] != -1:
                return memo[i]
            
            # I can either take 1 or 2 steps
            answ = cost[i]+min(dfs(i+1), dfs(i+2))

            # else store it in the memo
            memo[i] = answ

            return answ

        # might either take 1 or 2 steps for the very first step
        return min(dfs(0), dfs(1))