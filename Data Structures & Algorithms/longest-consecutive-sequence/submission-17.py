from typing import List
from collections import defaultdict

# soln to create a dict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_dict = defaultdict(int)

        max_counter = 0

        for value in nums:

            if value not in new_dict:

                if value+1 in new_dict and value-1 in new_dict:

                    # add the values that are after and before together
                    # this assumes that the value is a connecting value (3,4) (6,7) and value is 5
                    new_dict[value] = new_dict[value-1] + new_dict[value+1] + 1

                elif value-1 in new_dict:
                    new_dict[value] = new_dict[value-1] + 1
                
                elif value+1 in new_dict:
                    new_dict[value] = new_dict[value+1] + 1

                else:
                    new_dict[value] = 1

                # upating the lower values
                while value-1 in new_dict:
                    # updating all the values lesser than 
                    new_dict[value-1] = new_dict[value]
                    value-=1
                
                # upating the upper values
                while value+1 in new_dict:
                    new_dict[value+1] = new_dict[value]
                    value+=1         

                max_counter = max(max_counter, new_dict[value])

        return max_counter
