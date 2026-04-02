class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # checkin gof rempty
        if nums==[]:
            return 0

        # getting all the first values of the sequence
        first_val = []

        for value in set(nums):
            if value-1 not in set(nums):
                first_val.append(value)

        
        # loop throu all first values
        count = 1
        most_count = 1

        for value in first_val:

            while value+1 in set(nums):

                # increement counter
                count+=1
                most_count = max(most_count,count)

                # increment value
                value+=1

            # reset count
            count = 1

        return most_count