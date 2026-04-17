class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0

        # creating a unique set
        unique_nums = set(nums)
        first_val = []

        # find all the first value first
        for value in unique_nums:
            if value-1 not in unique_nums:
                first_val.append(value)


        max_counter = 0

        for value in first_val:

            counter = 0

            while value in unique_nums:
                # increment first value
                value+=1
                counter+=1
                max_counter = max(max_counter, counter)

        return max_counter

        