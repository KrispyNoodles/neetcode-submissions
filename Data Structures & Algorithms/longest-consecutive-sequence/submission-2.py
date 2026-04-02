# hash map
from typing import List
from collections import defaultdict

# using sorting
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # creating a defaultdict
        map_num = defaultdict(int)
        result = 0

        for value in nums:

            # ignore duplicates to preserve the logic
            if not map_num[value]:

                # lengths of existing left and right intervals
                left_len = map_num[value - 1]
                right_len = map_num[value + 1]
                
                # total merged length including current value
                total_len = left_len + right_len + 1

                # storing the value so that it will not look into this value again
                # and it allows for future merges
                map_num[value] = total_len 

                # updating the left boundary: move left_len steps left
                map_num[value - left_len] = total_len

                # updating the right boundary: move right_len steps left
                map_num[value + right_len] = total_len

                 # updating the best result
                result = max(result,map_num[value])
        
        return result