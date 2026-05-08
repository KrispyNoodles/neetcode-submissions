class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

                
        # one algo that finds out how big the island is and converts all these to 0
        def paintZero(r, c):

            # checking for oob, then paint the 1's
            if min(r,c)<0 or r==row or c==col or grid[r][c] == '0':
                return
            
            # finding the condition to paint
            if grid[r][c] == '1':
                grid[r][c] = '0'
          
            # explore
            paintZero(r+1,c)
            paintZero(r-1,c)
            paintZero(r,c+1)
            paintZero(r,c-1)
        
        for gr in grid:
            print(gr)

        row, col = len(grid), len(grid[0])
        counter = 0
        
        # one algo that finds a 1, then start working with the second algo
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                # call function
                if grid[r][c] == '1':
                    counter+=1
                    paintZero(r,c)

        return counter
            