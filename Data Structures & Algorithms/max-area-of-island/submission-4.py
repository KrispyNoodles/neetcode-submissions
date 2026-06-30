class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def helperFn(r,c, counter):

            # checking for oob
            if min(r,c)<0 or r==ROWS or c==COLS:
                return counter

            # checking if a 1 is found
            if grid[r][c]==1:

                # increment counter and convert to 0
                counter+=1
                grid[r][c]=0
            
            else:
                return counter

            # explore
            counter = helperFn(r,c+1, counter)
            counter = helperFn(r+1,c, counter)
            counter = helperFn(r,c-1, counter)
            counter = helperFn(r-1,c, counter)

            return counter 
            
        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    curr_counter = helperFn(r,c, 0)
                    answer = max(answer, curr_counter)
        return answer