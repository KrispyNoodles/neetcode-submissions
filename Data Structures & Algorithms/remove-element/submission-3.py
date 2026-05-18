class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # left will be the writer
        left = 0
        
        # moving
        for i in range(len(nums)):

            # this means it is a value we want to keep
            if nums[i] != val:

                # using left as a writer
                nums[left] = nums[i]
                left+=1
            
        return left