# REDOOOO!!! LOL
# it is an variation/appliocation of a decreasing montonic stack

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # put them as pairs together
        pos_speed = []

        for index in range(len(position)):
            time_took = (target-position[index])/speed[index]

            pos_speed.append((position[index], speed[index], time_took))
        
        # rearrange them first based on position
        # it must be reordered from furtherest-nearest
        # as the nearest will not be blocked by any
        sorted_sped = sorted(pos_speed, key=lambda x:x[0], reverse=False)

        # creating a stack now
        stack_num = []

        # this is an application of a decreasing monotonic stack
        # means the values in the stack are [5, 4, 3, 2, 1]

        # because it has to find all the large values of time as these will be the ones slowing all the cars behind on the left
        # (2.0, 4.67, 1.5)
        # stack will contain (4.67 and 1.5)

        # checkin from all to the second last
        # moving from left to right
        for car in sorted_sped:
            
            # if the car timing is longer than the one in the stack,
            # it has to follow this one instead
            while stack_num and car[2] >= stack_num[-1][2]:
                stack_num.pop()

            stack_num.append(car)
        
        return len(stack_num)
    
# time complexity of O(nlog(n)) because of the sorted triplet of all cars
# space compelxcity of O(n)