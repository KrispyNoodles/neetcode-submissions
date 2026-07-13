class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # typing BFS
        
        ROWS, COLS = len(heights), len(heights[0])

        # sets that contain the coordinate in which they can reach the pacific or the atlantic ocean
        pacific, atlantic = set(), set()


        def dfs(r,c, visit, prevHeight):
            
            # checking for oob
            if min(r,c)<0 or r==ROWS or c==COLS:
                return
            
            # checking it it has been visited before
            if (r,c) in visit:
                return 
            
            # checking if the current height is smaller than prevHeight
            # we are going out to in meaning the inner one/ the current one has 
            # to be bigger
            if heights[r][c]<prevHeight:
                return

            # visit the new cell
            visit.add((r,c))

            # recurssive call to explore
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])

        # checking the first row, of the pacific
        # and the last row, which refers to the atlantic
        # to see which other coordinates can reach there as well
        for c in range(COLS):

            # the prevheight to check if we can move to the next
            # initailise to be the same
            prevHeight = heights[0][c]
            dfs(0, c, pacific, prevHeight)

            prevHeight = heights[ROWS-1][c]
            dfs(ROWS-1, c, atlantic, prevHeight)

        # doing dfs for the sides of each ocean
        for r in range(ROWS):

            prevHeight = heights[r][0]
            dfs(r,0, pacific, prevHeight)

            prevHeight = heights[r][COLS-1]
            dfs(r,COLS-1, atlantic, prevHeight)

        answer = []

        # now we check for ever r and c, if it is in the pacific and atlantic ocean
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    answer.append([r,c])

        return answer


