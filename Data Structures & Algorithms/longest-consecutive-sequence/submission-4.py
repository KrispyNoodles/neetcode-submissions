# redo
from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        
        # sort first
        sort_nums = sorted(set(nums))

        max_counter = 1
        current_counter = 1
        i=0

        while i < len(sort_nums)-1:
            print(current_counter)

            if sort_nums[i]+1 == sort_nums[i+1]:
                current_counter += 1
                max_counter = max(max_counter, current_counter)
                
            else:             
                current_counter = 1

            i += 1
            
        return max_counter