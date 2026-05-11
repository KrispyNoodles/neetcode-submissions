
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # the standard BFS
        # BFS Structure
        queue = deque()
        visisted = set()

        rotten_fruit = []
        fresh_fruit = 0

        ROW, COL = len(grid), len(grid[0])

        # adding all the rotten banaanse in
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if grid[r][c]==2:

                    # the original queue will be the rotten babnana
                    queue.append((r,c))
                
                if grid[r][c]==1:
                    fresh_fruit+=1

        # if there is no fresh fruit, then there is nothing to infect
        if fresh_fruit==0:
            return 0
        if queue==[]:
            return -1

        time = 0
        infected_checker = False 


        while queue:

            infected_checker = False 

            for _ in range(len(queue)):

                r, c = queue.popleft()

                # condition that checks it is finished
                # like if it reaches the bottome right
                # or can just leave it to run forever

                # directions can move
                directions = [(0,1),(0,-1),(1,0),(-1,0)]

                for dr, dc in directions:

                    # new points
                    new_r, new_c = dr+r, dc+c

                    # checking for oob
                    if min(new_r, new_c)<0 or new_r==ROW or new_c==COL:
                        continue

                    # checking if it is empty
                    if grid[new_r][new_c]==0:
                        continue
                    
                    # if it reaches a fresh fruit
                    if grid[new_r][new_c]==1:
                        # replace the fruit
                        grid[new_r][new_c]=2
                        
                        # minus the total fresh fruit count by 1
                        fresh_fruit-=1

                        # it has infected one fruit
                        infected_checker= True

                        # add to the viisted and queue
                        queue.append((new_r, new_c))
                        visisted.add((new_r, new_c))


            if infected_checker:
                time+=1
        
        if fresh_fruit != 0:
            return -1

        else:
            return time

        