from typing import List

# bucket sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # because it is either 0,1 or 2
        bucket_arr = [0, 0, 0]

        for value in nums:
            bucket_arr[value] += 1

        index = 0
        
        for values in range(len(bucket_arr)):
            for _ in range(bucket_arr[values]):

                nums[index] = values
                index += 1
    
        return nums