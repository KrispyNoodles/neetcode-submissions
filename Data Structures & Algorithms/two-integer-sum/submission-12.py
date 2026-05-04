from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # creating a mapCount
        countMap = {}

        for index, value in enumerate(nums):
            
            # checking if the answe exist
            # and it is not the same
            if (target-value) in countMap.values():
                return [nums.index(target-value), index]
            
            # adding in
            if index not in countMap:

                # index has to be the key because it is unique
                countMap[index] = value