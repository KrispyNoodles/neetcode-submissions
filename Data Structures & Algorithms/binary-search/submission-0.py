from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            # using index function to find
            return nums.index(target)
        
        # it does not exist
        else:
            return -1