class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        answer = 0
        
        def dfs(r,c):

            # checking for oob 
            if min(r,c)<0 or r==ROWS or c==COLS:
                return

            if grid[r][c]=='0':
                return

            else:
                grid[r][c]='0'

            # explore the other areas
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]=='1':
                    dfs(r,c)
                    answer+=1


        return answer