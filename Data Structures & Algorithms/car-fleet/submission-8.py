# redoing again
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # putting the position speed and the time it takes to reach the target into a triplet
        pos_speed_time = []

        for index in range(len(position)):

            # time taken is distance divide by speed
            time_taken = (target-position[index])/speed[index]

            pos_speed_time.append((position[index], speed[index], time_taken))
        
        # reorder from furtherst from target to nearest
        ordered_pst = sorted(pos_speed_time, key=lambda x: x[0], reverse=False)

        # now create a stack that descends because we want to keep high timing and low timing across
        stack_num = []

        for cars in ordered_pst:
            
            # if the timinng is more, pop from the stack
            while stack_num and cars[2]>=stack_num[-1][2]:
                stack_num.pop()

            stack_num.append(cars)
        
        return len(stack_num)

# time complexity is O(nlog(n)) becasue of sorted list
# space complecxity is O(n)