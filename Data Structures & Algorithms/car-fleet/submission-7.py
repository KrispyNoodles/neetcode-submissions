from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # combining the target and position together into a triplet
        pos_speed = []

        for index in range(len(position)):

            position_of_car = position[index]
            speed_of_car = speed[index]
            time_taken = (target-position_of_car)/speed_of_car

            pos_speed.append((position_of_car, speed_of_car, time_taken))

        # sorting by distance, the one on the right will be lease affected
        sort_pos_speed = sorted(pos_speed, key=lambda x:x[0])

        # now we seach for the next higheest timing (including the last), as these are the timing that will affect on creating a fleet
        # decreasing monotonic
        val_stack = []

        for index in range(len(sort_pos_speed)):

            while val_stack and sort_pos_speed[index][-1] >= sort_pos_speed[val_stack[-1]][-1]:

                # remove the recent value from the stack
                val_stack.pop()

            val_stack.append(index)

        return len(val_stack)