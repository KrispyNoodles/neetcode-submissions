class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):

            if min(r,c)<0 or r==ROWS or c==COLS:
                return

            # if it is a water return
            if grid[r][c]=='0':
                return
            
            # explore the land and change to water
            grid[r][c]='0'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        answer =0 
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]=='1':
                    answer+=1
                    dfs(r,c)

        return answer