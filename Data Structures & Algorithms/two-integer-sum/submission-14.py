from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # creating a mapCount
        countMap = {}

        for index, value in enumerate(nums):
                        
            # checking if the answe exist and it is not the same
            # finding second val
            second_val = target-value

            if second_val in countMap.keys() and countMap[second_val]!=index:

                return [countMap[second_val], index]
            
            # adding in
            if value not in countMap:

                # index has to be the key because it is unique
                countMap[value] = index
