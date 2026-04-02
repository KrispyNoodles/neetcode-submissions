from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]
        
        # reduce the nums by one
        perms = self.permute(nums[1:])

        result = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p[:]

                # because the nums has been adjusted, therefore only use that value to plced within
                p_copy.insert(i, nums[0])
                result.append(p_copy)

        return result
