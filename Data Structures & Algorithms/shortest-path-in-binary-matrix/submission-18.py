from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # creating bfs
        ROWS, COLS = len(grid), len(grid[0])

        # visited and queue
        que = deque()
        visited = set()

        # adding the first dude in if it is not a 1
        if grid[0][0]!=1:
            que.append((0,0))
            visited.add((0,0))
        
        else:
            return -1

        # first one already
        answer = 1

        while que:

            for _ in range(len(que)):

                # pop
                r, c = que.popleft()

                # if reach the end return answer
                if r==ROWS-1 and c==COLS-1:
                    return answer

                directions = [[-1,+1],[+1,-1],[+1,+1],[-1,-1],[-1,0],[+1,0],[0,-1],[0,+1]]

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c

                    # checking for oob
                    if min(nr,nc)<0 or nr==ROWS or nc==COLS or (nr,nc) in visited:
                        continue

                    # checking also if it is a 1 then continue
                    if grid[nr][nc]==1:
                        continue

                    # else add into set
                    que.append((nr,nc))
                    visited.add((nr,nc))

            # increment once after moving through the queue
            answer+=1

        # means after everything still havent tio
        return -1