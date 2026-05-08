from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # from top left to bottom right
        start = (0,0)

        # checking if start is 1 if not return -1
        if grid[0][0]==1:
            return -1

        visisted = set()
        queue = deque()

        # add the first point into the start and queue
        visisted.add(start)
        queue.append(start)

        # Endpoint
        ROW, COL = len(grid), len(grid[0])
        
        # it will be incremented every time it moves to the next layer
        length = 1

        while queue:

            for _ in range(len(queue)):

                # pop_left
                r, c = queue.popleft()

                # checking if it has reached the end
                if r==ROW-1 and c==COL-1:
                    print('reached end')
                    return length

                # possibilites of path to move
                # left, right, up, down, and the 4 movements
                neighbours = [[0,1],[0,-1],[1,0],[-1,0], [1,1],[-1,-1],[1,-1],[-1,1]]

                for dr, dc in neighbours:

                    # checking for OOB
                    new_r, new_c = r+dr, c+dc

                    if min(new_r, new_c)<0 or new_r==ROW or new_c==COL:
                        continue
                    
                    # checking if it has been visited before or if it is a 1
                    if (new_r, new_c) in visisted or grid[new_r][new_c]==1:
                        continue
                    
                    # else, add the point into the queue and visited
                    visisted.add((new_r, new_c))
                    queue.append((new_r, new_c))

            # increment the lenght
            length+=1

        # no soln found
        return -1

# time compelxity of O(n*m) where n is row and m is col as each will be only visited once

