class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROW, COL = len(grid), len(grid[0])

        def helperFn(r,c):
            
            # checking for OOB, return
            if min(r,c)<0 or r==ROW or c==COL or grid[r][c]=="0":
                return
            
            # if it encounters the path that it can move then continue 
            # exploring and change it to 1
            else:
                grid[r][c]="0"

            helperFn(r+1,c)
            helperFn(r,c+1)
            helperFn(r-1,c)
            helperFn(r,c-1)


        answer = 0
        for r in range(ROW):
            for c in range(COL):

                # if island found explore!
                if grid[r][c]=="1":
                    answer+=1
                    helperFn(r,c)

        return answer