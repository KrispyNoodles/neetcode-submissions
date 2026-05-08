from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])

        # creating queue and set visited
        queue = deque()
        visited = set()

        fresh_fruit_count = 0

        time = 0

        fruit_infected = False

        # find all fresh and rotten fruits
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c]==1:
                    fresh_fruit_count+=1
                
                if grid[r][c]==2:

                    # adding the rotten fruit to it concurretnly
                    queue.append((r,c))
                    visited.add((r,c))

        # no rotten fruit to infect, therefore it is impossible
        if queue == []:
            return -1
        
        # no time needed for zero fresh fruits
        if fresh_fruit_count==0:
            return 0

        while queue:

            # reset the checker, before moving to each infected fruits
            fruit_infected = False

            for _ in range(len(queue)):

                r, c = queue.popleft()

                movements = [[0,1],[1,0],[0,-1],[-1,0]]

                for dr, dc in movements:
                    
                    new_r, new_c = dr+r, dc+c

                    # checking for oob
                    if min(new_r,new_c)<0 or new_r==ROW or new_c==COL:
                        continue

                    # check if it has been visited before
                    if (new_r, new_c) in visited:
                        continue

                    # checking if it is a ripe, bananana, then make it to become bad
                    if grid[new_r][new_c] == 1:

                        # else add in
                        queue.append((new_r,new_c))
                        visited.add((new_r,new_c))

                        # change to rotten
                        grid[new_r][new_c] = 2

                        # remove a fresh fruit, everytime it gets infected
                        fresh_fruit_count-=1
                        fruit_infected = True

            if fruit_infected:

                # increment counter
                time+=1

        # if there is still fresh fruit it means it cant be spread any further
        if fresh_fruit_count>=1:
            return -1
        else:
            return time
 

        


            


