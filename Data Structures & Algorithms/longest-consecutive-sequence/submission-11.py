class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0

        first_val = []

        # retrieving all first value
        for value in set(nums):
            if (value-1) not in set(nums):
                first_val.append(value)
        
        # checking how long each value can go
        # counter start from 1
        counter = 1
        max_counter = 1

        for value in first_val:

            while value+1 in set(nums):

                # increment the value to break the while loop counter
                value+=1

                # increment counter and update max_counter
                counter+=1

                max_counter = max(max_counter, counter)

            # else reset
            counter = 1

        return max_counter