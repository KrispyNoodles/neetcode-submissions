class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        start_arr = []
        set_nums = set(nums)

        for value in set_nums:
            if value-1 not in set_nums:
                start_arr.append(value)

        max_counter = 1

        for value in start_arr:

            counter = 1

            while value+1 in set_nums:
                value+=1
                counter+=1

            max_counter = max(max_counter,counter)

        return max_counter
        