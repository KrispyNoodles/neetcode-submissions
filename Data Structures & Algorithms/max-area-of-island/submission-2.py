class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_island = 0

        row, col = len(grid), len(grid[0])

        def island_counter(r,c):

            # check for oob
            if min(r,c)<0 or r==row or c==col or grid[r][c]==0:
                return 0

            # Mark as visited
            grid[r][c] = 0
            
            return 1+island_counter(r+1,c)+island_counter(r-1,c)+island_counter(r,c+1)+island_counter(r,c-1)


        # first algo to identify an island
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    
                    # island found
                    current_counter = island_counter(r, c)

                    # update
                    max_island = max(max_island, current_counter)
        
        return max_island
