from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # creating a set and a que
        que = deque()
        visited = set()

        if grid[0][0]==1:
            return -1

        # add in the top left
        que.append((0,0))
        visited.add((0,0))

        ROWS, COLS = len(grid), len(grid[0])

        length = 1

        # as long as there is a que
        while que:

            for _ in range(len(que)):

                r,c = que.popleft()

                # checking if we have reach the destination
                if r==ROWS-1 and c==COLS-1:
                    return length
                
                # the next neighbours
                neighbours = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

                for dr, dc in neighbours:

                    new_r, new_c = dr+r, dc+c

                    # checking if the new r and new c are oob move to the next point
                    if min(new_r, new_c)<0 or new_r==ROWS or new_c==COLS:
                        continue
                    
                    # if it has been visited before or it is not a place that we can go
                    if (new_r, new_c) in visited or grid[new_r][new_c]==1:
                        continue

                    # else add it into the que and visited
                    que.append((new_r,new_c))
                    visited.add((new_r,new_c))

            # add length after going through all the new points
            length+=1

        # if it doesnt reach the end, that means it will never reach
        return -1