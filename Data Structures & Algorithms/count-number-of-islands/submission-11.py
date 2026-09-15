class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # dfs algo
        def dfs(r,c):

            # checking for oob
            if min(r,c)<0 or r==ROWS or c==COLS:
                return

            if grid[r][c]=='0':
                return
            else:
                grid[r][c]='0'

            # explore
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        ROWS, COLS = len(grid), len(grid[0])

        answer =0
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]=='1':
                    answer+=1
                    dfs(r,c)

        return answer