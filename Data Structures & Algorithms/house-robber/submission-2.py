# having a saved memory
from typing import List

# Bottom Up/ Dynamic Programming
class Solution:
    def rob(self, nums: List[int]) -> int:

        # handling edge cases
        # no house and only 1 house
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        
        total_money = 0

        # dynamic array, saving the last 2 only
        dp = [0]*len(nums)

        # intialising
        # at index 0, rob that house
        dp[0] = nums[0]

        # at index 1, decide if I should rob 1 or 0
        dp[1] = max(nums[0], nums[1])

        # start from 2 to the len of nums
        for i in range(2, len(nums)):
            
            # decide to rob now or skip
            dp[i]=max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
