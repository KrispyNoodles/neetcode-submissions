class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        # creating two sets for pac and atl
        pac, atl = set(), set()

        def dfs(r,c,visited,prevHeight):

            # checking for OOB
            if min(r,c)<0 or r==ROWS or c==COLS:
                return
            
            # checking if it has been visited before
            if (r,c) in visited:
                return
            
            # checking if it is shorter than the prevheight, this means the water cant go into the land
            if heights[r][c]<prevHeight:
                return
            
            # else add to the visit
            visited.add((r,c))

            # exploration
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        # adding the top and bottom rows in
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        # adding the sides in
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        answer = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    answer.append([r,c])

        return answer

        