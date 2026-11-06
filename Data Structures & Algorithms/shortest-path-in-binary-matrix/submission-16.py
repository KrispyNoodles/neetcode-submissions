from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        # visited
        visited = set()
        queue = deque()

        # adding the first guy in if
        # if the first value is 1 we can no longer reach the end so
        if grid[0][0]==1:
            return -1
        
        visited.add((0,0))
        queue.append((0,0))

        answer = 1

        while queue:

            for _ in range(len(queue)):

                # popping the value
                r, c = queue.popleft()

                # checking if we have reached the end already
                if r==ROWS-1 and c==COLS-1:
                    return answer

                # directions that we can go
                directions = [[-1,0],[+1,0],[0,-1],[0,+1],[+1,+1],[-1,-1],[-1,+1],[+1,-1]]

                for dr, dc in directions:

                    nr, nc = dr+r, dc+c

                    # checking for oob
                    # then we skip adding it back to the queue
                    if min(nr,nc)<0 or nr==ROWS or nc==COLS or grid[nr][nc]==1 or (nr,nc) in visited:
                        continue

                    # else we add it to the queue and visited
                    queue.append((nr,nc))

                    visited.add((nr,nc))

            
                    # for each time we ruin the variable in the queue we increment couinter by 1
            answer+=1
    

        # if after veryhing never reach the end then return -1
        return -1
                