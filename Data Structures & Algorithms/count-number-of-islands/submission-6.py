class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        answer = 0
        ROWS, COLS = len(grid), len(grid[0])

        def helperFn(r,c):

            # checking for oob
            if min(r,c)<0 or r==ROWS or c==COLS:
                return
            
            # checking if it is a 0
            if grid[r][c]=="0":
                return
            
            # if 1, then continue
            # change 1 to 0
            grid[r][c]="0"

            helperFn(r+1,c)
            helperFn(r-1,c)
            helperFn(r,c+1)
            helperFn(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    answer+=1
                    helperFn(r,c)

        return answer
