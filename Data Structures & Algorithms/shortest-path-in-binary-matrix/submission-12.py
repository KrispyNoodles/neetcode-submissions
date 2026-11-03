from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        # checking if it is the top left
        if grid[0][0]==1:
            return -1

        # create queue and visit
        queue = deque()
        visited = set()

        # add the first point
        queue.append((0,0))
        visited.add((0,0))

        counter= 1

        while queue:

            for _ in range(len(queue)):
                r,c = queue.popleft()

                # if row reaches the end counter
                if r==ROWS-1 and c==COLS-1:
                    return counter

                # 8 directions can move
                directions= [[-1,0],[+1,0],[0,-1],[0,+1],[-1,-1],[+1,+1],[+1,-1],[-1,+1]]

                for dr, dc in directions:

                    # add the differece to r,c
                    nr, nc = dr+r, dc+c

                    # checking for oob
                    if min(nr,nc)<0 or nr==ROWS or nc==COLS or grid[nr][nc]==1 or (nr,nc) in visited:
                        continue

                    # else add it to the queue and visited
                    queue.append((nr,nc))
                    visited.add((nr,nc))
            
            # increment here because this is one step
            counter+=1
        
        # aftern running everything never reach the end return -1
        return -1
                