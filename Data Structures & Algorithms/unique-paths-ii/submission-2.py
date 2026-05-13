from typing import List

# Memoisation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # start from top left
        # end at bottom right
        # using normal method first

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        # creating another matrix which contains the numner of possibilites at each point
        # using -1 instead for paths with 0 possibilites
        cache_matrix = [[-1]*COL for _ in range(ROW)]

        # checking i
        # using dfs
        def dfs(r, c, cache):

            # checking if it is oob
            # only can move right or down so no need check for min()<0
            if r==ROW or c==COL:
                return 0
            
            # checking if it is blocked
            if obstacleGrid[r][c]==1:
                return 0
            
            # checking if it is inside
            if cache[r][c] != -1:
                return cache[r][c]

            # checking if it reached the end
            if r==ROW-1 and c==COL-1:
                return 1

            counter = 0

            counter += dfs(r+1,c, cache)
            counter += dfs(r,c+1, cache)

            # saving the answer
            cache[r][c] = counter

            return counter
        
        return dfs(0,0, cache_matrix)        