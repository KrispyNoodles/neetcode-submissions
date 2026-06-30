class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # count an island, the momment it counts change it to 0

        ROWS, COLS = len(grid), len(grid[0])

        def helperFn(r,c):

            # checking for oob
            if min(r,c)<0 or r==ROWS or c==COLS:
                return

            # checking if it is a land and convert
            if grid[r][c]=='1':
                grid[r][c]='0'
            else:
                return
            
            # exploring the other areas
            helperFn(r,c+1)
            helperFn(r+1,c)
            helperFn(r,c-1)
            helperFn(r-1,c)

        answer = 0 
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    helperFn(r,c)
                    answer+=1
        return answer