class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # sort first
        nums.sort()

        for index, value in enumerate(nums):
            if index!=value:
                return index

        return index+1