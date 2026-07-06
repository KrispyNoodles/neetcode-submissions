class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        answer = 0

        ROWS, COLS = len(grid), len(grid[0])

        def helperFn(r,c):

            # checking for oob
            if min(r,c)<0 or r==ROWS or c==COLS or grid[r][c]==0:
                return 0

            # increment the counter
            else:
                # change to water
                grid[r][c]=0

            counter = 0

            # explroe
            counter += helperFn(r+1,c)
            counter += helperFn(r,c+1)
            counter += helperFn(r,c-1)
            counter += helperFn(r-1,c)

            return counter+1

        
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]==1:
                    curr_island = helperFn(r,c)
                    answer = max(answer, curr_island)

        return answer
