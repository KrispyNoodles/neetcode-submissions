from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        # creating two sets for pac and atl
        pac, atl = set(), set()

        def bfs(r,c,visited,prevHeight):

            # adding the (r,c) into the queue and visited set
            queue.append((r,c))
            visited.add((r,c))

            while queue:

                for _ in range(len(queue)):

                    r,c = queue.popleft()

                    # update the prevHeight
                    prevHeight = heights[r][c]

                    directions = [[0,1],[1,0],[-1,0],[0,-1]]

                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc

                        # checking for oob
                        if min(nr,nc)<0 or nr==ROWS or nc==COLS:
                            continue
                        
                        # checking iif it is shorter than the prevHeight 
                        if heights[nr][nc]<prevHeight:
                            continue
                        
                        # checking if it is in visited
                        if (nr,nc) in visited:
                            continue
                        
                        # if it has pass all of this then continue
                        queue.append((nr,nc))
                        visited.add((nr,nc))


        # adding the top and bottom rows in
        for c in range(COLS):
            queue = deque()
            bfs(0,c,pac,heights[0][c])

            # refresh
            queue = deque()
            bfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        # adding the sides in
        for r in range(ROWS):
            queue = deque()
            bfs(r,0,pac,heights[r][0])

            queue = deque()
            bfs(r,COLS-1,atl,heights[r][COLS-1])

        answer = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    answer.append([r,c])

        return answer

        