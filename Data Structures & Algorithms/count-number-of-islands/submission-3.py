from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # create an overall counter
        counter = 0
        
        # traverse within the island using bfs
        # for each point that it has visited, convert the 1 into a 0

        ROWS, COL = len(grid), len(grid[0])

        # starign row and col
        def helper_fn(sr, sc):

            visited = set()
            queue = deque()

            # add the top left point
            visited.add((sr,sc))
            queue.append((sr,sc))

            while queue:

                for _ in range(len(queue)):

                    # pop_left
                    r, c = queue.popleft()

                    # getting all neighbours
                    neighbours = [[0,1],[1,0],[0,-1],[-1,0]]

                    # using the differences
                    for dr, dc in neighbours:

                        nr = dr+r
                        nc = dc+c

                        # checking for OOB
                        if min(nr,nc)<0 or nr==ROWS or nc==COL:
                            continue

                        if grid[nr][nc]=='0':
                            continue
                        else:
                            # convert the point into a 0
                            grid[nr][nc]='0'

                        visited.add((nr,nc))
                        queue.append((nr,nc))

                            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                # if point at grid is 1 then run function and increment counter
                if grid[r][c]=='0':
                    continue
                else:
                    counter+=1
                    helper_fn(r,c)

        return counter

            