## try solving again but using a smart prefix

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # creating a prefix and post fix
        total = sum(nums)

        current_sum = 0

        # current index will be the answer
        for index, value in enumerate(nums):

            # left_sum
            current_sum+=value
            left_sum = current_sum-value

            right_sum = total-left_sum-value

            # if leftsum is rightsum then answer is found
            if left_sum == right_sum:
                return index
                
        # after everything if doesnt work then return -1
        return -1