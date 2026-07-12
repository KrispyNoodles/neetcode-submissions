from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        # checking if top left is a 1
        if grid[0][0]==1:
            return -1

        queue = deque()
        visited = set()

        # adding the top left into the queue and visited
        queue.append((0,0))
        visited.add((0,0))

        counter = 1
        while queue:

            for _ in range(len(queue)):

                r,c = queue.popleft()

                # if reach the end return counter
                if r==ROWS-1 and c==COLS-1:
                        return counter

                directions = [[-1,1],[1,-1],[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1]]

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c

                    # checking for oob, or ==1 or visited before, move to the next direction,
                    if min(nr,nc)<0 or nr==ROWS or nc==COLS or grid[nr][nc]==1 or (nr,nc) in visited:
                        continue
                                    
                    # add it to the queue and visited
                    queue.append((nr,nc))
                    visited.add((nr,nc))
                
            counter+=1
        
        # if everything fail return -1
        return -1