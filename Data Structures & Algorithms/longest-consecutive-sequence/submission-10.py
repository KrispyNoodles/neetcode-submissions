class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        
        # creating a set of unique elements
        unique_nums = set(nums)

        first_num = []

        # identifying all first vals of the sequence
        for val in unique_nums:

            if val-1 not in unique_nums:
                first_num.append(val)

        length = 1
        max_length = 1
        # loop through the first num to find the max_len
        for val in first_num:

            while val+1 in unique_nums:

                # increment val
                val += 1

                length +=1

                # update maxlength
                max_length = max(max_length, length)

            # reset the legnth
            length = 1

        return max_length