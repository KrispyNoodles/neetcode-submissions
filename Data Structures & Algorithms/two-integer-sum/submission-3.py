from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):


            # finding the other values
            other_target = target - nums[i]

            # if the other_target is inside the array
            # and the index are different
            if other_target in nums:
                # finding the other_target index
                index_2 = nums.index(other_target)

                if index_2 != i:
                    return sorted([i, nums.index(other_target)])
