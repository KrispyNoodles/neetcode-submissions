from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        largest_len = 0

        # sort first the entire array from small to big
        sorted_values = sorted(nums)

        # create a temp array
        temp_arr = []
        # assume the first value is the begining of the biggest lenght

        for value in sorted_values:

            # if temp_arr is empty
            if not temp_arr:
                temp_arr.append(value)

            else:
                # check if the previous value inside is continous
                if value == temp_arr[-1] + 1:
                    temp_arr.append(value)

                # if the value is the same can just continue
                elif value == temp_arr[-1]:
                    continue

                else:
                    # reassign the max_leng
                    largest_len = max(largest_len, len(temp_arr))

                    # insert the value into the temp_arr
                    temp_arr = [value]


        # if it is just continuous, we have to compare between the empty and the temp_arr
        return max(largest_len, len(temp_arr))