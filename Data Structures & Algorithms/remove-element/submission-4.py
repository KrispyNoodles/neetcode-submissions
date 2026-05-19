class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        
        for i in range(len(nums)):

            if nums[i] != val:

                # write using left pointer
                nums[left] = nums[i]

                # shift left
                left+=1


        return left