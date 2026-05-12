# having a saved memory
from typing import List

# Memoization/ Top Down Dynamic Programming
class Solution:
    def rob(self, nums: List[int]) -> int:

        def helperFn(index, cache):

            # checking index is within range, if not no money to rob
            if index>=len(nums):
                return 0
            
            # checking if the answer exists in the cache
            if index in cache: 
                return cache[index]
        
            # can choose to either rob current house or next house
            # rob current or skip current
            cache[index] = max(nums[index] + helperFn(index+2, cache), helperFn(index+1, cache))
            
            return cache[index]

        # starting with index 0
        return helperFn(0, {})
