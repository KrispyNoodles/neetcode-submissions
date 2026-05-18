from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # since the first element is always unique
        left = 1

        # i will represent the fast
        for right in range(1, len(nums)):

            if nums[right]!=nums[right-1]:

                # we copy it to the left writer
                nums[left]=nums[right]

                # then increment left
                left+=1

        print(nums)
        return left