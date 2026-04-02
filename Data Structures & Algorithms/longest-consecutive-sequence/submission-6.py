from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        
        # sort first
        set_nums = set(nums)


        max_counter = 1
        current_counter = 1
        
        start_arrs = []

        # O(n)
        for number in set_nums:
            if (number-1) not in set_nums:
                start_arrs.append(number)


        # O(n)
        for starts in start_arrs:
            while starts+1 in set_nums:
                # update the current counter and max counter
                current_counter += 1
                starts+=1

                max_counter = max(max_counter, current_counter)

            # if outside while loop resets
            current_counter=1

        return max_counter
    
# time complexityt of O(n)