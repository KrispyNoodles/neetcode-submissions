from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # creating a prefix and post fix
        total = 0
        prefix = []
        postfix = []
        
        for i in nums:
            total+=i
            prefix.append(total)
        
        total = 0
        for index in range(len(nums)-1,-1,-1):
            total+=nums[index]
            postfix.append(total)

        postfix=postfix[::-1]


        for index in range(len(prefix)):

            left_sum = prefix[index-1] if index > 1 else 0
            right_sum = postfix[index+1] if index < len(prefix)-1 else 0
            
            if left_sum==right_sum:
                return index

        # after everything if doesnt work then return -1
        return -1