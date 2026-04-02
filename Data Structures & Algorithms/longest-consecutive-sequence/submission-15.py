from typing import List

# soln to find a first values of the sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        # creating a set once
        set_nums = set(nums)

        first_val_seq = []

        # getting first values of sequence
        for value in set_nums:
            if value-1 not in set_nums:
                first_val_seq.append(value)
        
        max_counter = 1

        for value in first_val_seq:

            # reset the counter to be 1
            counter = 1

            while value+1 in set_nums:

                # increment counter and value
                value+=1
                counter+=1

            # update the max_value when it breaks the loop
            max_counter = max(counter, max_counter)

        return max_counter
        
# time complexity of O(n^2) it reads each value once because of the set
# space complexity of O(n) in a situation where the array is as large as the first_val_seq