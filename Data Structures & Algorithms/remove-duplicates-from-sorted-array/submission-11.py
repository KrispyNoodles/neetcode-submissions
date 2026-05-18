class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        left = 1

        for i in range(1, len(nums)):

            # if the value is differnet then activate the writer
            if nums[i] != nums[i-1]:

                # reassign and shift left
                nums[left] = nums[i]
                left+=1
        
        return left

            