from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # creating a mapCount
        countMap = {}

        for index, value in enumerate(nums):
                        
            # checking if the answe exist and it is not the same
            # finding second val
            second_val = target-value

            if second_val in nums:
                # find index
                second_index = nums.index(second_val)

                if second_index != index:
                    answer = sorted([index, second_index])
                    return answer
# time complexity of O(n)