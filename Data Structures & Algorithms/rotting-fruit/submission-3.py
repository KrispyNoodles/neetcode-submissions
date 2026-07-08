from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # standard BFS
        queue = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0

        # assume that all rotten bananas are the starting point
        for r in range(ROWS):
            for c in range(COLS):

                # rotten
                if grid[r][c]==2:
                    queue.append((r,c))
                    visited.add((r,c))

                elif grid[r][c]==1:
                    fresh+=1

        # if fresh no more means finish liao
        if fresh == 0:
            return 0

        counter = 0
        while queue:
            for _ in range(len(queue)):

                r, c = queue.popleft()

                directions = [[0,1],[1,0],[-1,0],[0,-1]]

                for dr, dc in directions:

                    nr, nc = r+dr, c+dc

                    # checking for OOB
                    if min(nr, nc)<0 or nr==ROWS or nc==COLS:
                        continue
                    
                    # or if in visited or empty then move to next
                    if (nr, nc) in visited or grid[nr][nc]==0:
                        continue


                    # else if it is a fresh banana, then infect
                    if grid[nr][nc]==1:
                        
                        # minus fresh and change to infected
                        fresh-=1
                        grid[nr][nc]=2

                        # then add to queue and visited
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            
            counter+=1

        # checking if there is still any fresh
        if fresh==0:
            return counter-1
        else:
            return -1
