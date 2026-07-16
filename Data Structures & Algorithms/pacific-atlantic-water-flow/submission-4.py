class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()

        # depth first serach
        def dfs(r,c, visited, prevHeight):

            # checking if it is oob
            if min(r,c)<0 or r==ROWS or c==COLS:
                return

            # checking if it has been visited before
            if (r,c) in visited:
                return
            
            # if the current height is shorter than the prev height
            if heights[r][c]<prevHeight:
                return 

            # add it into the set
            visited.add((r,c))

            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
        
        # adding the first and last row of the ocean in
        for c in range(COLS):
            # pac
            dfs(0,c, pac, heights[0][c])
            # atl
            dfs(ROWS-1,c, atl, heights[ROWS-1][c])
        
        # first and last col
        for r in range(ROWS):
            dfs(r,0, pac, heights[r][0])
            dfs(r,COLS-1, atl, heights[r][COLS-1])

        # checking for overlapps coordinates
        answer = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    answer.append([r,c])

        return answer

