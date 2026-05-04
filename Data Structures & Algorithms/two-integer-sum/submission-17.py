from typing import List

# optimised map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # creating a mapCount
        countMap = {}

        for index, value in enumerate(nums):
                        
            # checking if the answe exist and it is not the same
            # finding second val
            second_val = target-value

            # no need to check second index, as it will find first before adding in
            if second_val in countMap:

                return [countMap[second_val], index]
            
            # adding in by default, because if it is already inside, it would have exited the for loop above
            # index has to be the key because it is unique
            countMap[value] = index

# time complexity of O(n)