from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        
        # creating sorted array
        set_val = set(nums)
        current_counter = 1
        max_counter = 1

        start_array = []

        # finding the first values of each starting seq
        for value in set_val:

            if (value-1) not in set_val:
                start_array.append(value)

        for value in start_array:

            while value+1 in set_val:

                # increment the counter
                current_counter+=1

                value+=1

                # update the max_counter
                max_counter = max(max_counter, current_counter)

            # if break then reset the current_coutner to be 1
            current_counter = 1
        
        return max_counter




