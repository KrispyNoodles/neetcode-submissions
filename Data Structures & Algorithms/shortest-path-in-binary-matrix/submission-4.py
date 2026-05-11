from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        visited  = set()

        ROW, COL = len(grid), len(grid[0])

        if grid[0][0]==1:
            return -1

        length = 1

        # adding the first point
        queue.append((0,0))
        visited.add((0,0))

        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()

                # checking if it has reached the destination
                if r == ROW-1 and c==COL-1:
                    return length

                # can move 8 points
                neighbours = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

                for dr, dc in neighbours:

                    # the new point moving
                    new_r, new_c = r+dr, c+dc

                    # checking for OOB
                    if min(new_r, new_c)<0 or new_r==ROW or new_c==COL:
                        continue

                    # checking that you can move into those points
                    if (new_r, new_c) in visited or grid[new_r][new_c]==1:
                        continue 

                    # else add it in
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))

            length+=1
        
        # if there is no length found
        return -1

            

