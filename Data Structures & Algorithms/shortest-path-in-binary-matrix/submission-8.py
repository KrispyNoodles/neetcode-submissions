from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # find the length of shortest path
        ROWS, COLS = len(grid), len(grid[0])

        # if starting or end is 1, can never solve
        if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
            return -1

        # visited
        visited = set()

        # queue
        que = deque()

        # adding the topleft to the queue and visited
        que.append((0,0))
        visited.add((0,0))

        length = 1

        while que:

            for _ in range(len(que)):

                # pop left from the que
                r,c = que.popleft()

                # checking if at destination, return answer
                if r == ROWS-1 and c==COLS-1:
                    return length

                neighbours = [[1,1],[-1,-1],[1,-1],[-1,1],[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in neighbours:

                    # new points
                    nr, nc = dr+r, dc+c

                    if min(nr,nc)<0 or nr==ROWS or nc==COLS:
                        continue
                    
                    # checking if it is already in the visited
                    # or they cannot move because it is a 1
                    if (nr,nc) in visited or grid[nr][nc]==1:
                        continue

                    # if not continue add these new points into the que and visited
                    que.append((nr,nc))
                    visited.add((nr,nc))

            # everytime you move
            length+=1
        
        # if never reach destination and que used finish, then it reached an error
        return -1