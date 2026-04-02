class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for index in range(len(nums)):
            
            # while the current index is less than the length
            # and the current value is the same as the next element
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                
                # removing the duplicates not to return the duplicates
                nums.pop(index)
        
        return len(nums)
