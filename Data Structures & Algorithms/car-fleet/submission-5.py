# REDOOOO!!! LOL
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # put them as pairs together
        pos_speed = []

        for index in range(len(position)):
            time_took = (target-position[index])/speed[index]

            # rounding to 2dp
            time_took = round(time_took, 2)

            pos_speed.append((position[index], speed[index], time_took))
        
        # rearrange them first based on position
        sorted_sped = sorted(pos_speed, key=lambda x:x[0], reverse=False)

        # creating a stack now
        stack_num = []

        # checkin from all to the second last
        for car in sorted_sped:

            # while the current's car speed is faster then the stack
            # then the stack should be poped!
            while stack_num and car[2]>=stack_num[-1][2]:
                stack_num.pop()

            stack_num.append(car)
    
        return len(stack_num)