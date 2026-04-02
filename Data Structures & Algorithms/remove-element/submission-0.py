from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0

        index = 0

        # for all values in the array
        while index < len(nums):

            # if the array is the same as the value
            if nums[index] == val:

                # pop it then append the underscore at the end
                nums.pop(index)
                index = index - 1
                nums.append('_')
                count+=1

            index += 1

        print(nums)

        return len(nums)-count
